# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
from twisted.enterprise import adbapi
import MySQLdb
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from spider_project.cnblogs_spider import settings


class CnblogsSpiderPipeline:
    def process_item(self, item, spider):
        return item


class JsonWithEncodingPipeline(object):
    # 自定义JSON文件的导出
    def __init__(self):
        self.file = codecs.open("article.json", "a", encoding="utf-8")
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # 将数据转换为字符串
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    def spider_close(self, spider):
        self.file.close()


class MysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect("127.0.0.1", 'root', 'root', 'article_spider', charset='utf-8')

    def process_item(self, item, spider):
        # 全字段插入
        insert_sql = """
             insert into jobbole_article(title, url, front_image_path)
             values (%s, %s, %s)
         """
        params = list()
        params.append(item["title"])
        params.append(item["url"])
        params.append(item["front_image_path"])

        self.sursor.execute(insert_sql, tuple(params))
        self.cursor.commit()
        return item


# mysql异步插入
class MysqlTwistedPipeline(object):
    # 异步插入:重载类方法
    @classmethod
    def from_settings(cls, seetings):
        # from
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQ_PASSWORG"],
            charset='utf-8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
