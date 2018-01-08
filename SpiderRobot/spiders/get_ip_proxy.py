# -*- coding: utf-8 -*-
import scrapy
import requests
from SpiderRobot.items import IPItem

class GetIpSpider(scrapy.Spider):
    """用来抓取代理IP
    """
    name = "get_ip_proxy"
    allowed_domains = ['http://www.xicidaili.com/']
    start_urls = [
            'http://www.xicidaili.com/nn/1', #国内高匿代理
            'http://www.xicidaili.com/nn/2', #国内高匿代理
            'http://www.xicidaili.com/nt/1', #国内普通代理
            'http://www.xicidaili.com/nt/2', #国内普通代理
            'http://www.xicidaili.com/wt/1', #国内HTTP代理
            'http://www.xicidaili.com/wt/2', #国内HTTP代理
    ]

    custom_settings = {
            'ITEM_PIPELINES': {
                'SpiderRobot.pipelines.IPProxyPipeline': 1,
            }
    } 
    
    def parse(self, response):
        """parse"""
        try:
            table = response.xpath('//table[@id="ip_list"]')
            print table
            
            trs = table.xpath('//tr')[1:]   #去掉标题行
            items = {}
            for i in range(100):
                pre_item = IPItem()
                pre_item['ip_address'] = trs[i].xpath('td[2]/text()').extract()[0]
                pre_item['ip_port'] = trs[i].xpath('td[3]/text()').extract()[0]
                pre_item['ip_speed'] = trs[i].xpath('td[7]/div/@title').re('\d+\.\d*')[0]
               
                ip_str = pre_item['ip_address'] + ":" + pre_item['ip_port']
                if(self.verify_proxy(ip_str)):
                    items[i] = ip_str

                #if(pre_item['ip_speed'] <= "1"): #筛选高速度的ip
                #    ip_str = pre_item['ip_address'] + ":" + pre_item['ip_port']
                #    items[i] = ip_str
            
            #print items
            return items
        except Exception as e:
            print str(e)

    def verify_proxy(self, ip):
        """用来测试ip代理是否有用"""
        
        ip_proxy = {
                "http": "http://"+ip,
        } 
        try:
            if requests.get('http://wenshu.court.gov.cn', proxies=ip_proxy, timeout=5).status_code == 200:
                print  '%s can use' % ip_proxy
            return True
        except Exception as e:
            #print ('fail %s' % ip_proxy)
            #print str(e)
            return False 
