# -*- coding: utf-8 -*-
import scrapy
from Scrapy.items import IthomeItem

# XPath
# class[last()]
# class[0]
# class[position()]

# 1 scrapy startproject <project_name>

# 2 scrapy genspider <demo_name> 待爬的网页

# 3 scrapy crawl <demo_name>


class IthomeSpider(scrapy.Spider):
    name = 'ithome'
    allowed_domains = ['ithome.com']
    start_urls = ['http://it.ithome.com/']

    def parse(self, response):
        name=response.xpath("//div[@class='block new-list-1']/ul/li/span[@class='title']/a/text()").extract()[0]
        items={}
        items['frist']=name
        return items









