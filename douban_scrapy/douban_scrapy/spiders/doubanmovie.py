import scrapy
from lxml import etree, html
from ..items import DoubanScrapyItem
# from scrapy.utils.project import get_project_items

'''
豆瓣排名数据动态加载获取不到
'''

class DoubanmovieSpider(scrapy.Spider):
    name = "doubanmovie"
    allowed_domains = ["movie.douban.com"]
    # start_urls = ["https://movie.douban.com"]
    offset = 0
    url = "https://movie.douban.com/top250?start="
    start_urls = (
        url + str(offset),
    )
    start = ["url"]
    # print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))



    def parse(self, response, *args, **wkargs):
        item = DoubanScrapyItem()

        '''问题一：
        xpath和 CSS Selector选择器爬取出来的内容在这里不一样
        Xpath爬出来的数据有问题
        '''
        # print(response.text)
        # 将html转化为element元素
        # ele = etree.HTML(response.text)
        # print(response.text)
        movies = response.xpath("//div[@class='info']")
        # content > div > div.article > ol > li:nth-child(2) > div > div.info
        # movies = response.css("#content > div > div.article > ol > li > div > div.info")
        # movies = response.css("div.info")
        # print(movies1)
        print("获取")
        print(movies)
        print(len(movies))
        # content > div > div.article > ol > li:nth-child(2) > div > div.info

        for each in movies:
            print(each)
            '''
            extract()返回的是一个列表，列表里的每个元素是一个对象，
            extract()把这些对象转换成Unicode字符串
            '''
            # 电影标题
            print("开始")
            # l = each.xpath("//div[@class='item']//span[@class='title']/text()").extract()[0]
            # print(l)
            # str_title = each.xpath(".//span[@class='title'][1]/text()").extract()[0]
            # item['title'] = ['{}'.format(str_title)]
            item['title']= each.xpath(".//span[@class='title'][1]/text()").extract()[0]
            print(item['title'])
            # 电影信息
            # str_bd = each.xpath(".//div[@class='bd']/p/text()").extract()[0]
            # item['bd'] = ['{}'.format(str_bd)]
            item['bd']= each.xpath(".//div[@class='bd']/p/text()").extract()[0]

            # 豆瓣评分
            # str_star = each.xpath(".//span[@class='rating_num']/text()").extract()[0]
            # item['star'] = ['{}'.format(str_star)]
            item['star']= each.xpath(".//span[@class='rating_num']/text()").extract()[0]

            # 脍炙人口的一句话
            quote = each.xpath(".//p[@class='quote']/span/text()").extract()
            print(type(quote))
            if len(quote) != 0:
                # str_quote = quote[0]
                # item['quote'] = ['{}'.format(str_quote)]
                item['quote']= quote[0]

            print("结束")
            yield item

        if self.offset < 255:
            print("到这里了")
            self.offset += 25
            print(self.offset)
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

