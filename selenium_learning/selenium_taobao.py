from selenium import webdriver
# selenium请求超时触发
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
#
from selenium.webdriver.support import expected_conditions as EC
# 设置等待时间
from selenium.webdriver.support.ui import WebDriverWait
# 将汉字汉字转义
from urllib.parse import quote
# pyquery解析页面和lxml、bs4一样
from pyquery import PyQuery
import time


'''
        淘宝安全策略：需要登录
        
'''


# 静态变量：不变的——>大写（官方规定）
KEYWORD = 'ipad'

driver_optons = Options()
driver_path = r"D:\Compiler Files\Python\Python310\Scripts\msedgedriver.exe"
# 打开已存在的窗口
driver_optons.add_experimental_option("debuggerAddress", "127.0.0.1:9225")
browser = webdriver.Edge(options=driver_optons)
# browser = webdriver.Edge()
# 设置等待时间wait = 10
wait = WebDriverWait(browser, 20)


def crawl_page(page):
    print("执行")
    try:
        url = 'https://s.taobao.com/search?q='+quote(KEYWORD)
        print(url)
        browser.get(url)

        # 安全策略解决：
        # 沉睡15秒——扫码登录
        time.sleep(5)

        '''
                 等待一定的时间，（时间为之前设置wait的时间）
                 在wait = 10秒的时间内，一直等待里面这段代码执行结束
                 如果超时没有找到，则继续向后执行
        '''
        if page > 1:
            print(1)
            page_box = wait.until(
                # 该元素可不可以定位——>定位
                EC.presence_of_element_located((By.CSS_SELECTOR, '.next-pagination-pages .next-input input'))
            )
            print(2)
            submit_button = wait.until(
                # 该元素可不可以点击——>定位
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, ".next-pagination-jump-go")
                )
            )
            print(3)
            page_box.clear()
            print(3.1)
            # 输入要跳转的页面
            page_box.send_keys(page)
            print(3.2)
            # 点击跳转确定
            submit_button.click()
            print(3.3)

        # 跳转到另一个函数去
        print("跳转")
        get_products()

        # 在等待时间内完成定位
        wait.until(
            # 用里面的东西，定位需要的元素：presence_of_element_located
            EC.presence_of_element_located(
                # 使用CSS_SELETOR解析器进行定位
                (By.CSS_SELECTOR, ".Content--contentInner--QVTcU0M")
            )
        )

    except:
        crawl_page(page)


def get_products():
    # 获取网页源代码
    data = browser.page_source
    # 解析页面源代码
    doc = PyQuery(data)
    # 48个商品
    print(4)
    items = doc('div.Content--contentInner--QVTcU0M div a.Card--doubleCardWrapper--L2XFE73').items()
    i = 0
    for item in items:
        i = i + 1
        print(i)
        product = {
            'img':item.find('img.MainPic--mainPic--rcLNaCv').attr('src'),
            'price':'{0}{1}{2}'.format(item.find('.Price--unit--VNGKLAP').text(), item.find('.Price--priceInt--ZlsSi_M').text(), item.find('.Price--priceFloat--h2RR0RK').text()),
            'deal':item.find('.SalesPoint--subIconWrapper--s6vanNY ').text(),
            'title':item.find('.Title--title--jCOPvpf').text(),
            'shop':item.find('.ShopInfo--shopName--rg6mGmy a').text(),
            'location':item.find('.Price--procity--_7Vt3mX').text()
        }
        print(product)




crawl_page(3)

