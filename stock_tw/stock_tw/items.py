# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockTwItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class StockItem(scrapy.Item):
    date    = scrapy.Field()
    close   = scrapy.Field()
    volume  = scrapy.Field()
    open    = scrapy.Field()
    high    = scrapy.Field()
    low     = scrapy.Field()