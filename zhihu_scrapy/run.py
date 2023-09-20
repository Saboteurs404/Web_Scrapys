import os
import sys

from scrapy import cmdline

path = os.path.dirname(os.path.abspath(__file__))
print(path)
sys.path.append(path)

cmdline.execute("scrapy crawl zhihu".split())
