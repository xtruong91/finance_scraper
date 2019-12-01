# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IndexesUsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TimeFrame(scrapy.Item):
    DATE    = scrapy.Field()
    CLOSE   = scrapy.Field()
    VOLUME  = scrapy.Field()
    OPEN    = scrapy.Field()
    HIGH    = scrapy.Field()
    LOW     = scrapy.Field()


class TradeFile(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
