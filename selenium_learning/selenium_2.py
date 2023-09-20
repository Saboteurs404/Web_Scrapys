import time

# 无界面浏览器设置

from selenium import webdriver
from selenium.webdriver.common.by import By

Edge_options = webdriver.EdgeOptions()
Edge_options.add_argument('--headless')
browser = webdriver.Edge(options = Edge_options)

url = 'https://finance.sina.com.cn/realstock/company/sh600519/nc.shtml'
browser.get(url)
data = browser.page_source
print(data)

time.sleep(20)
browser.quit()
