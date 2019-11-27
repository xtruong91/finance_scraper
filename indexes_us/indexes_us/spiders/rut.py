# -*- coding: utf-8 -*-
import scrapy
import json
from lxml import etree
from indexes_us.items import TimeFrame


class RutSpider(scrapy.Spider):
    name = "rut"
    allowed_domains = ["www.nasdaq.com"]
    start_urls = [
        "https://www.nasdaq.com/market-activity/index/rut/historical"
    ]
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "indexes_us.middlewares.RotateProxyMiddleware": 300,
            "indexes_us.middlewares.RotateAgentMiddleware": 301,
            "indexes_us.middlewares.NasdaqMiddleware": 302
        },
        "ITEM_PIPELINES": {
            "indexes_us.pipelines.IndexPipeline": 300
        }
    }

    def parse(self, response):

        frame = TimeFrame()

        # traverse each page
        for i in json.loads(response.body):

            data = etree.HTML(i)

            # locate table
            frame_xpath = ".//tbody[@class=\"historical-data__table-body\"]/tr"
            frame_list = data.xpath(frame_xpath)

            # fill items
            for j in frame_list:

                frame['DATE'] = j.xpath('./th[1]/text()')[0]
                frame['CLOSE'] = j.xpath('./td[1]/text()')[0][1:]
                frame['VOLUME'] = j.xpath('./td[2]/text()')[0]
                frame['OPEN'] = j.xpath('./td[3]/text()')[0][1:]
                frame['HIGH'] = j.xpath('./td[4]/text()')[0][1:]
                frame['LOW'] = j.xpath('./td[5]/text()')[0][1:]
                yield frame
