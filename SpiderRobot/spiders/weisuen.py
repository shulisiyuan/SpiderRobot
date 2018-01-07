# -*- coding: utf-8 -*-
import scrapy
from SpiderRobot.items import SpiderrobotItem

class WeisuenSpider(scrapy.Spider):
    name = 'weisuen'
    #allowed_domains = ['sina.com']
    #start_urls = [
    #        'http://news.sina.com.cn/c/nd/2017-12-26/doc-ifypxrpp4277754.shtml',
    #        'http://news.sina.com.cn/c/nd/2017-12-27/doc-ifyqchnr6116620.shtml',
    #        'http://news.sina.com.cn/w/2017-12-27/doc-ifyqchnr6070358.shtml',
    #]

    #def parse(self, response):
    #    item = SpiderrobotItem()
    #    item["urlname"] = response.xpath("/html/head/title/text()")
    #    
    #    my_str = ""
    #    for i in item["urlname"].extract():
    #        my_str = i.encode('UTF-8')
    #    
    #    item["urlname"] = my_str
    #    print item['urlname']
    #    #return item

    #这一步很重要，为spider指定需要执行的pipeline
    custom_settings = {
            'ITEM_PIPELINES': {
                'SpiderRobot.pipelines.SpiderrobotPipeline': 1,
            }
    } 

    def start_requests(self):
        url = 'http://wenshu.court.gov.cn/CreateContentJS/CreateListDocZip.aspx?action=1'

        # FormRequest 是Scrapy发送POST请求的方法
        yield scrapy.FormRequest(
            url = url,
            formdata = {"conditions": "%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B%E4%B8%BA%E6%B0%91%E4%BA%8B%E6%A1%88%E4%BB%B6%E4%B8%94%E5%85%B3%E9%94%AE%E8%AF%8D%E4%B8%BA%E7%A6%BB%E5%A9%9A",
                        "docids": "f00b6b07-b647-11e3-84e9-5cf3fc0c2c18|黄东妹与梁飞离婚纠纷再审审查民事裁定书|2013-04-07",
                        "keyCode": ""},
            callback = self.parse_page
        )
    
    def parse_page(self, response):
        print "得到Response"
        print response.status
        #print response.body

        item = SpiderrobotItem()
        item['url'] = response.url
        item['files'] = response.body
        return item

