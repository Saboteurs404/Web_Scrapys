import scrapy
# python3
from urllib import parse


class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ["https://www.zhihu.com"]
    # 模拟登录需加上 COOKIES_ENABLED:TRUE
    custom_settings = {
        "COOKIES_ENABLED": True
    }

    # def start_requests(self):
        # 在这里模拟登录拿到cookie就可以了
        # """
        # 两种滑动验证码识别方案：
        # - 1、使用opencv识别
        # - 2、使用机器学习方法识别
        # :return:
        # """



    '''
        parse()是Spider的一个方法，被调用时，
        每个初始化URL完成下载后生成的response对象将会作为唯一的参会传递给该函数，
        该方法负载解析返回的数据（response.data） 提取数据（生成item）以及生成需要进一步处理的URL的request对象
    '''
    def parse(self, response, *args, **kwargs):
        '''
        提取出html页面所有的URL，并根据这些URL进行进一步爬取
        如果提取的URL中格式为/questioin/xxx就下载之后直接进入解析函数

        :param response:
        :return:
        '''
        print("1")
        all_urls = response.css("a::attr('href')").extract()
        print(all_urls)
        # 列表生成式
        all_urls = [parse.urljoin(response.url, url) for url in all_urls]
        # url去重
        all_urls =
        for url in all_urls:
            pass
        print("进来了", all_urls)
        return all_urls








