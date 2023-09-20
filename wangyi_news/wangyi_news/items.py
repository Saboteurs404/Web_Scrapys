# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义爬取的注意
    news_thread = scrapy.Field()
    news_title = scrapy.Field()
    nwws_url = scrapy.Field()
    news_time = scrapy.Field()
    news_source = scrapy.Field()
    source_url = scrapy.Field()
    news_body = scrapy.Field()


