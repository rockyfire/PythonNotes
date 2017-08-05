# -*- coding: utf-8 -*-
import scrapy
from weather.items import chanyoujiuItem
from weather.settings import *

import random

class ChanyoujiSpider(scrapy.Spider):
    name = 'chanyouji'
    allowed_domains = ['chanyouji.com']
    start_urls = ['http://chanyouji.com/']

    # 下载器中间件实现

    # def active_ip(self):
    #     with open("data/active.txt") as f:
    #         line=f.readlines()
    #         active_ip=[]
    #         for i in range(0,len(line)):
    #             active_ip.append("".join(line[i].split('\n')))
    #         return random.choice(active_ip)
    #
    #
    # def __init__(self):
    #     DEFAULT_REQUEST_HEADERS['http']=self.active_ip()
    #     self.header=DEFAULT_REQUEST_HEADERS


    def parse(self, response):
        item=chanyoujiuItem()
        item['img']=response.xpath("//img/@src").extract()
        yield item

