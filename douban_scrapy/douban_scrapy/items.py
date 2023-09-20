# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #  电影标题
    title = scrapy.Field()

    # 电影信息
    bd = scrapy.Field()

    # 豆瓣电影
    star = scrapy.Field()

    # 脍炙人口的一句话
    quote = scrapy.Field()

    pass
