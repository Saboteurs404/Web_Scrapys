__author__ = 'xlh'

import os.path
import sys

from scrapy import cmdline

# date : 2023/9/4

path = os.path.dirname(os.path.abspath(__file__))
print(path)
sys.path.append(path)

cmdline.execute("scrapy crawl doubanmovie".split())

