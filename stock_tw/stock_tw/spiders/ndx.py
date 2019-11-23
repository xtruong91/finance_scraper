# -*- coding: utf-8 -*-
import scrapy
import json
from lxml import etree
from stock_tw.items import StockItem


class NdxSpider(scrapy.Spider):
    name = 'ndx'
    allowed_domains = ['www.nasdaq.com']
    start_urls = ["https://www.nasdaq.com/market-activity/index/ndx/historical"]

    def parse(self, response):
        
        item = StockItem()

        for i in json.loads(response.body):
            data = etree.HTML(i)
            stock_list = data.xpath('.//tbody[@class="historical-data__table-body"]/tr')
            for j in stock_list:
                item['date']= j.xpath('./th[1]/text()')[0]
                item['close'] = j.xpath('./td[1]/text()')[0][1:]
                item['volume'] = j.xpath('./td[2]/text()')[0]
                item['open'] = j.xpath('./td[3]/text()')[0][1:]
                item['high'] = j.xpath('./td[4]/text()')[0][1:]
                item['low'] = j.xpath('./td[5]/text()')[0][1:]
                yield item

        