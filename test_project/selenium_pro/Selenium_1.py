from selenium import webdriver
import time

browser = webdriver.Edge()

# 设置浏览器全屏
browser.maximize_window()
browser.get("https://www.baidu.com")
time.sleep(2)

# 打开哔哩哔哩页面
browser.get("https://www.bilibili.com/")
time.sleep(2)

# 后退到百度页面
browser.back()
time.sleep(2)

# 前进到哔哩哔哩页面
browser.forward()
time.sleep(2)

# 关闭浏览器
browser.close()
