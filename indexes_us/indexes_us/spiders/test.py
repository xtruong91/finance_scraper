# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'indexes_us.middlewares.RotateProxyMiddleware': 300,
            'indexes_us.middlewares.RotateAgentMiddleware': 301,
            'indexes_us.middlewares.SeleniumMiddleware': 302
        }
    }
