# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PoolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ProxyItem(scrapy.Item):
    PROXY = scrapy.Field()


class AgentItem(scrapy.Item):
    AGENT = scrapy.Field()