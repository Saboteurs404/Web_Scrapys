import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Edge()

driver.get("https://www.baidu.com")

# 隐形等待，判断网页是否加载完成。如果未完成则会报超时加载
# driver.implicitly_wait(20)

# 获取百度输入框的位置信息
input_box = driver.find_element(by=By.CSS_SELECTOR, value='.s_ipt')

mouse_left = ActionChains(driver)

# 模拟鼠标左击搜索框
mouse_left.click(input_box).release(input_box).perform()

# 清除该输入中的原本内容
input_box.clear()

# 模拟输入文本
input_box.send_keys("这是一个输入测试")

# # 模拟键盘输入enter进行跳转————>成功
# input_box.send_keys(Keys.ENTER)

# 获取搜索按钮的位置
search_button = driver.find_element(by=By.ID, value="su")

# 模拟鼠标左击， 进行搜索
mouse_left = ActionChains(driver)
mouse_left.click(search_button).release(search_button).perform()

# 等待时间
time.sleep(10)
