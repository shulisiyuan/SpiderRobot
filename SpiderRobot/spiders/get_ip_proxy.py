# -*- coding: utf-8 -*-
import scrapy
from SpiderRobot.items import IPItem

class WeisuenSpider(scrapy.Spider):
    name = "get_ip_proxy"
    allowed_domains = ['http://www.xicidaili.com/']
    start_urls = [
            'http://www.xicidaili.com/nn/',
            'http://www.xicidaili.com/nt/',
            'http://www.xicidaili.com/wt/',
    ]


    def parse(self, response):
        table = response.xpath('//table[@id="ip_list"]')[0]
        trs = table.xpath('//tr')[1:]   #去掉标题行
        items = {}
        for i in range(50):
            pre_item = IPItem()
            pre_item['ip_address'] = trs[i].xpath('td[2]/text()').extract()[0]
            pre_item['ip_port'] = trs[i].xpath('td[3]/text()').extract()[0]
            pre_item['ip_speed'] = trs[i].xpath('td[7]/div/@title').re('\d+\.\d*')[0]
            
            if(pre_item['ip_speed'] <= "1"): #筛选高速度的ip
                ip_str = pre_item['ip_address'] + ":" + pre_item['ip_port']
                items[i] = ip_str
        #print items
        #print
        return items
