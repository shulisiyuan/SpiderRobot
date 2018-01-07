# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#导入codecs模块，可以使用codecs模块直接进行编解码
import codecs

class SpiderrobotPipeline(object):
    """SpiderrobotPipeline is to process item 
    """

    def __init__(self):
        """__init__"""
        self.savefile = codecs.open("/home/xuhaoguang/work/project/SpiderRobot/SpiderRobot/docs/mydata.doc", "wb")

    def process_item(self, item, spider):
        """process_item"""
        #line = item['urlname'] + "\n"

        self.savefile.write(item['files'])
        return item

    def close_spider(self, spider):
        """close_spider"""
        self.savefile.close()
        #print "爬虫结束"

class IPProxyPipeline(object):
    """用来存储ip代理
    """
    def __init__(self):
        """__init__""" 
        #print "进入pipeline的__init__"
        self.ip_proxy_file = codecs.open("/home/xuhaoguang/work/project/SpiderRobot/SpiderRobot/ip_proxy.txt", "wb")

    def process_item(self, item, spider):
        """process_item"""
        #print "进入process_item"
        #print item
        for k, v in item.iteritems():
            #print v
            self.ip_proxy_file.write(v + "\n")
        return item
        
    def close_spider(self, spider):
        """close_spider"""
        self.ip_proxy_file.close()
        #print "爬虫结束"
