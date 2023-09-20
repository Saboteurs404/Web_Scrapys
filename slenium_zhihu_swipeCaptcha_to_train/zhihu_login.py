'''
获取知乎登页面的滑动验证码
收集这些验证码为训练做准备
'''
import os
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options

from slenium_zhihu_swipeCaptcha_to_train.train_complete import train_complete

# # 全局
# # 浏览器对象
#
# options = Options()
# options.add_experimental_option('excludeSwitches', ['enable-automatoin'])
# browser = webdriver.Edge(options=options)


class get_vericication():

    # 跳转到密码登录方式
    def code_to_pwd(self):

        # 验证码登录方式
        code_button = browser.find_element(by=By.XPATH, value="//div[@class='SignFlow-tabs']/div[1]")
        print(code_button.text)

        # 密码登录方式
        pwd_button = browser.find_element(by=By.XPATH, value="//div[@class='SignFlow-tabs']/div[2]")
        print(pwd_button.text)

        # 鼠标移动到密码登录方式左击， 不需要,release()否则页面会关闭
        mouse_left = ActionChains(browser)
        mouse_left.move_to_element(pwd_button).pause(1).click(pwd_button).perform()

    def login(self):
        # 用户名输入框：
        UserName_Box = browser.find_element(by=By.XPATH, value="//input[@name='username']")

        # 密码输入框
        Pwd_Box = browser.find_element(by=By.XPATH, value="//input[@name='password']")

        # 清空并输入用户名
        UserName_Box.clear()
        UserName_Box.send_keys(username)

        # 情况并输入密码
        Pwd_Box.clear()
        Pwd_Box.send_keys(passwd)

        # 输入回车键确认
        Pwd_Box.send_keys(Keys.ENTER)

    def saving_img(self):

        # 保存验证码
        # 获取验证码背景图片位置
        background_img = browser.find_element(by=By.CLASS_NAME, value="yidun_bg-img")
        # 保存图片src
        img = background_img.get_attribute('src')
        # 通过requests发送一个get请求到图片地址，返回的响应是图片内容
        picture = requests.get(img)
        # print(picture.content)

        # 保存图片
        path = './images/slider/train_slider.jpg'

        # 将获取到的图片二进制流写到本地
        # 'wb+':删除并重新打开
        with open(path, 'wb+') as f:
            # 对图片类型通过picture.content方式访问响应内容，将相应内容写入baidu.png中
            f.write(picture.content)

    def refresh(self):

        # 刷新验证码
        # 验证码刷新位置
        refresh = browser.find_element(by=By.CLASS_NAME, value="yidun_refresh")

        mouse_left = ActionChains(browser)
        # 左击刷新按钮
        mouse_left.click(refresh).release(refresh).perform()

    def slider(self):
        # 实例化train_complete()类
        train = train_complete()
        response_dic = train.get_response()

        # 判断位置信息是否存在
        if response_dic == None:
            return "训练内容为空"
        elif response_dic['results'] == None:
            return "训练结果为空"
        elif response_dic['results'][0] == None:
            return "位置信息为空"
        elif response_dic['results'][0]['location'] == None:
            return "位置信息内容为空"
        else:
            left = response_dic['results'][0]['location']['left']
            print("滑动验证码距左侧的距离为：{}".format(left))

        self.matching(left)

    def matching(self, left):

        slider_button = browser.find_element(by=By.XPATH, value="//div[@class='yidun_control']/div[2]")
        print("获取成功", slider_button.get_attribute('class'))
        mouse_draganddrop = ActionChains(browser)
        mouse_draganddrop.drag_and_drop_by_offset(slider_button, left+10, 0).release(slider_button).perform()


if __name__ == '__main__':
    edge_options = Options()
    # 设置为开发模式
    driver = "D:/Compiler Files/Python/Python310/Scripts/msedgedriver.exe"
    # 配置浏览器
    edge_options.add_experimental_option("debuggerAddress", "127.0.0.1:9225")
    # edge_options.add_experimental_option('excludeSwitches', ['enable-automatoin'])
    browser = webdriver.Edge(options=edge_options)

    # 知乎
    url = 'https://www.zhihu.com/signin'
    browser.get(url)
    # 保存验证码的数量
    n = 20
    username = "18734694207"
    passwd = '19990106.'

    # 实例化类
    sc = get_vericication()
    # 进行密码登录
    sc.code_to_pwd()
    # 输入信息并确认
    sc.login()
    # 强制等待
    time.sleep(1)
    # 保存验证码
    sc.saving_img()
    # # 滑动验证码
    sc.slider()
    time.sleep(10)
    browser.quit()
    # time.sleep(100)
