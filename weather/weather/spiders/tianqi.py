# -*- coding: utf-8 -*-
import scrapy

from weather.items import tianqiItem


class TianqiSpider(scrapy.Spider):
    name = 'tianqi'
    allowed_domains = ['tianqi.com']
    start_urls = []

    location=['putian','guangzhou']

    for i  in location:
        start_urls.append("http://"+i+".tianqi.com")

    def parse(self, response):
        items=[]
        for s in response.xpath('//div[@class="tqshow1"]'):
            item = tianqiItem()
            item['site']=s.xpath('h3').xpath('string(.)').extract()
            item['weekday']=s.xpath('p').xpath('string(.)').extract()
            item['img']=s.xpath('ul/li[@class="tqpng"]/img/@src').extract()
            item['temperature']=s.xpath('ul/li[2]').xpath('string(.)').extract()
            item['state']=s.xpath('ul/li[3]/text()').extract()
            item['wind']=s.xpath('ul/li[@style="height:18px;overflow:hidden"]/text()').extract()
            items.append(item)

        return items


