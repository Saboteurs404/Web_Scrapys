import os.path
import sys

from scrapy.cmdline import execute

'''
# 编写脚本文件启动爬虫项目
# pycharm相较于cmd启动的好处的方便调试
'''

# 查询；路径文件位置
print(__file__)
# 项目根目录
# print(os.path.dirname(__file__))
# 项目绝对路径
# print(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(["scrapy", "crawl", "cnblogs"])