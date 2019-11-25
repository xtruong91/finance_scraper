from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from indexes_us.spiders.spx import SpxSpider
from indexes_us.spiders.ndx import NdxSpider

setting = get_project_settings()
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner(setting)

d = runner.crawl(SpxSpider)
d = runner.crawl(NdxSpider)
d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()
