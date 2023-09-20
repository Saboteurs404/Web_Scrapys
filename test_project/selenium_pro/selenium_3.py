from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://finance.sina.com.cn/")

# 类名查找
class_name = driver.find_elements(by=By.CLASS_NAME, value='m-hdline')
print(1)
print(class_name[0].text)

# 输出新闻标题
title = driver.find_elements(by=By.CSS_SELECTOR, value="div.m-hdline a.liveNewsLeft")
print(2)
print(title[0].text)

# 文本中内容部分匹配
partial_link_text = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value="王传福")
print(3)
for i in range(len(partial_link_text)):
    print(partial_link_text[i].text)

# 匹配文本中的全部内容
link_text = driver.find_elements(by=By.LINK_TEXT, value="王传福、李振国重磅发声")
print(4)
print(link_text[0].text)
