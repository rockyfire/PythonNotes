# -*- coding: utf-8 -*-
import scrapy

from weather.items import proxyIPItem
from weather.settings import *



class ProxyipSpider(scrapy.Spider):
    name = 'proxyIp'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/nn/1']


    # 下载延迟或者设置User-Agent
    # def __init__(self):
    #     self.header=DEFAULT_REQUEST_HEADERS

    def parse(self, response):
        s=response.xpath("//tr[@class='odd']")
        for content in s:
            item=proxyIPItem()
            item['ip']=content.xpath("td[2]/text()").extract()
            item['port']=content.xpath("td[3]/text()").extract()
            yield item

