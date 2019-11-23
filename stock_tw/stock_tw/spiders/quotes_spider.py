import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.nasdaq.com/market-activity/index/ndx/historical',
    ]

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)