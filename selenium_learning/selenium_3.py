import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.maximize_window()
browser.get('https://news.cnblogs.com/n/748239/')
data = browser.page_source
time.sleep(30)
print(data)
