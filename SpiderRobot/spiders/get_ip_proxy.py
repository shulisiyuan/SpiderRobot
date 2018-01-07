# -*- coding: utf-8 -*-
import scrapy
from SpiderRobot.items import IPItem

class GetIpSpider(scrapy.Spider):
    """用来抓取代理IP
    """
    name = "get_ip_proxy"
    allowed_domains = ['http://www.xicidaili.com/']
    start_urls = [
            'http://www.xicidaili.com/nn/', #国内高匿代理
            'http://www.xicidaili.com/nt/', #国内普通代理
            'http://www.xicidaili.com/wt/', #国内HTTP代理
    ]

    custom_settings = {
            'ITEM_PIPELINES': {
                'SpiderRobot.pipelines.IPProxyPipeline': 1,
            }
    } 
    
    def parse(self, response):
        """parse"""
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
