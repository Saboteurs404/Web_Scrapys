# from urllib.request import Request
import re
import json
import scrapy
# from cssselect import Selector
from scrapy import Selector
import undetected_chromedriver
# from selenium import
from scrapy import selector, Request
from urllib import parse
import requests

class CnblogsSpider(scrapy.Spider):
    name = "cnblogs"
    allowed_domains = ["news.cnblogs.com"]
    start_urls = ["https://news.cnblogs.com"]

    custom_settings = {
    # 当COOKIES_ENABLED设置为True的时候scrapy就会把settings的cookie关掉，使用自定义cookie
        "COOKIES_ENABLED": True
    }

    def parse(self, response):
        """
        1、获取新闻列表页中的新闻url并交给scrapy进行下载，下载后调用调用相应的解析方法
        2、获取下一页的URL并交给scrapy进行下载，下载完成后交给parse继续跟进
        :param response:
        :return:
        """
        # print(response.text)
        # 获取到每条新闻的链接
        urls = response.css('div#news_list h2 a::attr(href)').extract()
        print(urls)
        # post_nodes = response.css('#news_list .news_block').extract()
        post_nodes = response.css('#news_list .news_block')[:2]
        print(post_nodes)
        print('-------------------------------')
        print(len(post_nodes))
        for post_node in post_nodes:
            # print(1)
            print("进入循环")
            print(post_node)
            #  Selector 是一个可以独立使用的模块。
            #  我们可以直接利用 Selector 这个类来构建一个选择器对象，
            #  然后调用它的相关方法如 xpath()、css() 等来提取数据
            # post_node = Selector(text=post_node)
            # print("post_node")
            # print(post_node)
            # 嵌套CSS
            '''
            报错：'str' object has no attribute 'css'
            解决：，直接将其进行强制转换为Selector
            Selector(text=person).css()
            '''
            image_url = post_node.css('.entry_summary a img::attr(src)').extract_first("")
            print(image_url)
            print(response.url)
            post_url = post_node.css('h2 a::attr(href)').extract_first("")
            # 生成器yield
            # 判断URL是否是完整路径
            # if not post_url.startswith("http"):
            #     yield Requests(url = "{}{}".format("https://news.cnblogs.com/", post_url))

            # 优化：可以自动判断post_url是否是完整路径
            # yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url":image_url}, callback=self.parse_detail)

        # 提取下一页并交给scrapy进行下载
        next_url = response.css("div.pager a:last-child::text").extract_first("")
        # if next_url == "Next >":
        #     next_url = response.css("div.pager a:last-child::attr(href)").extract_first("")
        #     yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)
        yield Request(url='https://news.cnblogs.com/n/750077/', callback=self.parse_detail)
        # 优化：next_url = response.xpath("//div[@class='pager']//a[contains(text(), 'Next >')]/@href").extract_first("")
    def parse_detail(self, response):

        print("到这里了")
        print(response.url)
        match_re = re.match(".*?(\d+)", response.url)
        # ?是非贪婪匹配
        # 。*？就是尽可能的少匹配， 后面一旦出现\d他就会匹配数字
        # 如果正则表达式中出现了括号，那么第一个括号里面的内容是group(1)，第二是group(2)
        print(match_re)
        if match_re:
            title = response.css("#news_title a::text").extract_first("")
            create_date = response.css("#news_info .time::text").extract_first("")
            content = response.css("#news_content").extract()
            print(content)
            tag_list = response.css(".news_tags a::text").extract()
            tags = ','.join(tag_list)
            print(1)
            print(tag_list)

            # 同步代码
            post_id = match_re.group(1)
            html = requests.get(parse.urljoin(response.url, "NewsAjax/GetAjaxNewsInfo?contentId={}".format(post_id)))
            j_data = json.loads(html.text)

            # # 异步代码
            # yield Request(url=parse.urljoin(response.url, "NewsAjax/GetAjaxNewsInfo?contentId={}".format(post_id)), callback=self.parse)

            praise_nums = j_data["DiggCount"]
            fav_nums = j_data["TotalView"]
            comment_nums = j_data["CommentCount"]

        def parse_nums(self, response):
            pass

