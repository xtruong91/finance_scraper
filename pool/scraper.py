from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from pool.spiders.agent import AgentSpider
from pool.spiders.proxy import ProxySpider

setting = get_project_settings()
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner(setting)

d = runner.crawl(AgentSpider)
d = runner.crawl(ProxySpider)
d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()
