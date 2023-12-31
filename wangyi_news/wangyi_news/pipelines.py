# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter


class WangyiNewsPipeline:

    def __init__(self):
        self.file = open('news_data.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, encodings='utf-8')
        self.exporter.start_exporting()

    def close(self, spider):
        self.exporter = CsvItemExporter(self.file, encodings='utf-8')
        self.file.close()

    def process_item(self, item, spider):
        return item
