# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random

from SpiderRobot.settings import UAPOOL #ippool is added inadvanced
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy import signals

class UAPOOLS(UserAgentMiddleware):
    """select ip proxy for spider
    """
    def __init__(self, ua = ''):
        """init
        """
        print "进入到UAPOOLS.__init__方法"
        self.user_agent = ua
    
    def process_request(self, request, spider):
        """process_request
        """ 
        print "进入到UAPOOLS.process_request方法"
        thisua = random.choice(UAPOOL)
        print "当前使用的ua是 " + thisua
        request.headers.setdefault('User-Agent', thisua)
