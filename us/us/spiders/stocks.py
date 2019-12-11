# -*- coding: utf-8 -*-
import scrapy
import loguru
from datetime import date
from us.items import HistoryFile


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    allowed_domains = ['www.nasdaq.com']
    start_urls = ['http://www.nasdaq.com/']
    custom_settings = {
        "ITEM_PIPELINES": {
            "us.pipelines.StockPipeline": 300
        }
    }

    def parse(self, response):

        stocks = ["aapl", "amzn", "tsla", "nflx", "msft"]

        for s in stocks:
            history = HistoryFile()
            url_tpl = (
                "https://www.nasdaq.com/api/v1/historical/"
                "{stock}/"
                "stocks/"
                "{start}/"
                "{end}"
            )
            today = date.today()
            start = "{y}-{m}-{d}".format(y=today.year - 5,
                                         m=today.month,
                                         d="0" + str(today.day) if (today.day < 10) else today.day)
            end = "{y}-{m}-{d}".format(y=today.year,
                                       m=today.month,
                                       d="0" + str(today.day) if (today.day < 10) else today.day)
            url = url_tpl.format(stock=s.upper(),
                                 start=start,
                                 end=end)
            loguru.logger.info(url)
            history["file_urls"] = [url]
            yield history
