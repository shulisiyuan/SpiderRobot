# -*- coding: utf-8 -*-
import scrapy

class WenshuSpider(scrapy.Spider):
    """WenshuSpider
    """
    name = 'wenshu'
    #allowed_domains = ['wenshu.court.gov.cn']
    #start_urls = [
    #        'http://wenshu.court.gov.cn/List/List',
    #]

    #def parse(self, response):
    #    """parse
    #    """
    #    print response.body

    def start_requests(self):
        url = 'http://wenshu.court.gov.cn/List/ListContent'

        # FormRequest 是Scrapy发送POST请求的方法
        yield scrapy.FormRequest(
            url = url,
            formdata = {
                "Param": "案件类型:民事案件",
                #"Param": "%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B%3A%E6%B0%91%E4%BA%8B%E6%A1%88%E4%BB%B6%2C%E5%85%B3%E9%94%AE%E8%AF%8D%3A%E7%A6%BB%E5%A9%9A",
                "Index": "2",
                "Page": "5",
                "Order": "法院层级",
                "Direction": "asc",
                },
            callback = self.parse_page
        )
    
    def parse_page(self, response):
        print "得到Response"
        #print response.status
        print response.body

        #item = SpiderrobotItem()
        #item['url'] = response.url
        #item['files'] = response.body
        return item

