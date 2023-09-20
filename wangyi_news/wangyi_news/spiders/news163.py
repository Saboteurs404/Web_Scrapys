import requests
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import WangyiNewsItem


# https://www.163.com/news/article/IEHCGDU3000189FH.html
# https://www.163.com/news/article/IEHAPL8L000189FH.html
# https://www.163.com/news/article/IEHCF8GM000189FH.html
# https://www.163.com/news/article/IEHCGDU3000189FH.html
# https://www.163.com/news/article/IEHCENJ9000189FH.html

# https://www.163.com/news/article/\.*?html

class News163Spider(CrawlSpider):
    name = "news163"
    allowed_domains = ["news.163.com"]
    start_urls = ["https://news.163.com"]

    # 深度优先爬虫
    # follow:是否允许深入
    # callback:回调函数

    # 抓取页面
    print("在这里")
    rules = (Rule(LinkExtractor(allow=r'/article/.*?html'), callback="parse_item", follow=True),)
    # print()
    print(rules)
    htmls = requests.get('https://news.163.com')
    # print(htmls.text)
    print("到这里")

    def parse_item(self, response):

        print("回调")
        # print(response.text)
        print(response.url)
        item = WangyiNewsItem()
        item['news_thread'] = response.url.split().split('/')[-1][:-5]
        self.get_title(response, item)
        self.get_time(response, item)
        return item

    def get_title(self, response, item):
        title = response.css('.post_title::text').extract()
        if title:
            print("title:{}".format(title[0]))
            item['news_title'] = title[0]

    def get_time(self, response, item):
        time = response.css("div.post_info::text").extract()
        if time:
            print("data:{}\n".format(time[0].strip().replace('来源: ', '')))
            item["news_time"] = time[0].strip().replace('来源: ', '')
