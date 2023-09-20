from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
browser.get("https://finance.sina.com.cn/")

# 隐形等待，判断网页是否加载完成。如果未完成则会报超时加载
browser.implicitly_wait(10)
data = browser.page_source
print(type(data))

# 使用elements进行多元素查找，结果会被保存到列表里
news_titles = browser.find_elements(by=By.CSS_SELECTOR, value="div.m-hdline a")
print(news_titles[0].text)

# 获取新闻跳转链接
news_hrefs = browser.find_elements(by=By.XPATH, value="//div[@class='m-hdline']//a[@target='_blank'][1]")
print(news_hrefs[0].get_attribute('href'))
new_href = news_hrefs[0]
print(new_href.text)

# 点击鼠标左键操作 点击第一天新闻
mouse_left = ActionChains(browser)
mouse_left.click(new_href).release(new_href).perform()


time.sleep(20)