#coding = utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 模拟键盘鼠标操作

#browser = webdriver.Chrome() #谷歌
browser = webdriver.Edge()
# 网页最大化
browser.maximize_window()
browser.get("http://www.baidu.com")
# page_source用于获取网页的源代码，然后可以使用正则表达式、CSS、XPath、bs4来解析代码
data = browser.page_source
# print(browser.page_source)

# 1、使用XPath来定位元素
# 新版本Selenium的一些改变
input = browser.find_element(By.XPATH, '//*[@id="kw"]').send_keys("selenium")
print(input)
#通过id = kw定位百度输入框，通过键盘方法send_keys()向输入框中输入selenium。
browser.find_element(By.XPATH, '//*[@id="su"]').click()
#通过id=su定位搜索按钮，并向按钮发送单击事件click()
'''
# 2、使用css_selector来定位元素
#kw
#su
input_1 = browser.find_element(By.CSS_SELECTOR, '#kw').send_keys("python")
print(input_1)
browser.find_element(By.CSS_SELECTOR, '#su').click()
'''
time.sleep(20)
browser.quit()