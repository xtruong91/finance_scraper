# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter


class IndexesUsPipeline(object):
    def process_item(self, item, spider):
        return item


class NasdaqPipeline(object):

    def __init__(self, file_name):
        self.file = open("../data/indexes_us/" + file_name.upper() + "_5Y.csv", "wb")
        self.exporter = CsvItemExporter(self.file)

    @classmethod
    def from_crawler(cls, crawler):
        file_name = getattr(crawler.spider, "name")
        return cls(file_name)

    def open_spider(self, spider):

        self.exporter.start_exporting()

    def process_item(self, item, spider):

        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):

        self.exporter.finish_exporting()
        self.file.close()
