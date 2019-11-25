# -*- coding: utf-8 -*-
import scrapy
from pool.items import ProxyItem


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = ['free-proxy-list.net']
    start_urls = ['http://free-proxy-list.net']
    custom_settings = {
        'ITEM_PIPELINES': {
            'pool.pipelines.ProxyPipeline': 301
        }
    }

    def parse(self, response):

        proxy = ProxyItem()

        for row in range(1, 21):

            ip = response.xpath("//tbody/tr[{row}]/td[1]/text()".format(row=row)).get()
            port = response.xpath("//tbody/tr[{row}]/td[2]/text()".format(row=row)).get()
            proxy["PROXY"] = "{ip}:{port}".format(ip=ip, port=port)
            self.logger.debug("{ip}:{port}".format(ip=ip, port=port))

            yield proxy

