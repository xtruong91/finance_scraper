# -*- coding: utf-8 -*-
import scrapy
from pool.items import AgentItem


class AgentSpider(scrapy.Spider):
    name = 'agent'
    allowed_domains = ['deviceatlas.com']
    start_urls = ['https://deviceatlas.com/blog/list-of-user-agent-strings']
    custom_settings = {
        'ITEM_PIPELINES': {
            'pool.pipelines.AgentPipeline': 301
        }
    }

    def parse(self, response):

        new_agent = AgentItem()

        agent_list = response.xpath("//td").getall()
        for agent in agent_list:

            new_agent["AGENT"] = agent
            yield new_agent
