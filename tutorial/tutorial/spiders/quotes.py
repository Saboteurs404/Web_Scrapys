import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/page/1/',
                  'http://quotes.toscrape.com/page/2/']

    def parse(self, response):
        '''
        测试代码
        ____________________________________________
        :param response:
        :return:
        '''

        # page = response.url.split('/')[-2]
        # print(page)
        # filename = 'quotes-{}.html'.format(page)
        # with open(filename, 'wb') as f:
        #     # w:创建文件， b:二进制模式
        #     f.write(response.body)
        # # 打印日志
        # self.log('Saved file {}'.format(filename))

        '''
        ____________________________________________
        '''
        # 获取所有名言
        quotes = response.css(".quote")

        # 存储数据
        page = response.url.split("/")[-2]
        filename = 'quote-{}.txt'.format(page)
        with open(filename, 'wb') as f:
            # 获取每条名言内的具体属性
            for quote in quotes:
                content = quote.css(".text::text").extract()[0]
                author = quote.css(".author::text").extract()[0]
                tags = quote.css(".tags .keywords::attr('content')").extract()

                print("content:\n", content)
                print("author\n", author)
                print("tags:\n", tags)
                f.write('content:{}\n author:{}\n tags:{}\n'.format(content, author, tags).encode())




