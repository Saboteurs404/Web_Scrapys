from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("https://www.zhihu.com/signin?next=%2F")


time.sleep(100)