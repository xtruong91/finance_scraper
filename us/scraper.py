from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from us.spiders.indexes import IndexesSpider
from us.spiders.stocks import StocksSpider

setting = get_project_settings()
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})


class USScraper():

    def __init__(self):
        self.runner = CrawlerRunner(setting)
        self.runner.crawl(IndexesSpider)
        self.runner.crawl(StocksSpider)
        d = self.runner.join()
        d.addBoth(lambda _: reactor.stop())

    def scrape(self):
        reactor.run()
