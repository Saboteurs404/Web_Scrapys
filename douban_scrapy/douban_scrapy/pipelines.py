# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

'''
编写Pipelines管道文件（把数据存储到MongoDB）
'''

import pymongo
from scrapy.utils.project import get_project_settings

class DoubanScrapyPipeline:
    def __init__(self):
        settings = get_project_settings()
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        user = settings["MONGODB_USER"]
        psw = settings["MONGODB_PSW"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]

        # 链接数据库
        # # 数据库登录需要账号密码的话
        mongo_url = 'mongodb://admin:root@localhost:27017/?authMechanism=DEFAULT'
        # self.client = pymongo.MongoClient(mongo_url)
        # self.db = self.client[dbname]

        # 创建MongoDB数据库链接
        # client = pymongo.MongoClient(host = host, port = port)
        client = pymongo.MongoClient(mongo_url)

        # 身份认证：
        # client.authenticate(user, psw)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库名
        self.sheet = mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        print("获取的将要存入数据库的数据：")
        print(data)
        # pymongo4.0 中Collection.insert()方法被移除，使用 Collection.insert_one 或者 Collection.insert_many 替代：
        if data:
            self.sheet.insert_one(data)
        return item

    # def close_spider(self):
    #     self.client.close()