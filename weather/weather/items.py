# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class tianqiItem(scrapy.Item):
    site=scrapy.Field()
    weekday=scrapy.Field()
    img=scrapy.Field()
    temperature=scrapy.Field()
    state=scrapy.Field()
    wind=scrapy.Field()


class proxyIPItem(scrapy.Item):
    ip=scrapy.Field()
    port=scrapy.Field()


