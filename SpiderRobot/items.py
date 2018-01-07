# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderrobotItem(scrapy.Item):
    url = scrapy.Field()
    files = scrapy.Field()

class IPItem(scrapy.Item):
    """代理ip
    """
    ip_address = scrapy.Field()
    ip_port = scrapy.Field()
    ip_speed = scrapy.Field()
