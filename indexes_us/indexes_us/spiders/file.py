# -*- coding: utf-8 -*-
import scrapy
import loguru
from datetime import date
from indexes_us.items import TradeFile


class FileSpider(scrapy.Spider):
    name = "file"
    allowed_domains = ["www.nasdaq.com"]
    start_urls = [
        "https://www.nasdaq.com"
    ]
    custom_settings = {
        "ITEM_PIPELINES": {
            "indexes_us.pipelines.NasdaqPipeline": 300
        }
    }

    def parse(self, response):

        indexes = ["ndx", "spx", "nya", "ixic", "rut"]

        for i in indexes:

            # new data holder
            new_file = TradeFile()
            url_tpl = (
                "https://www.nasdaq.com/api/v1/historical/"
                "{index}/"
                "index/"
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
            url = url_tpl.format(index=i.upper(), start=start, end=end)
            loguru.logger.info(url)
            new_file["file_urls"] = [url]
            yield new_file
