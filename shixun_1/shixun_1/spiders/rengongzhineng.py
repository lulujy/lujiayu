# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

class Rengongzhineng(CrawlSpider):

    name = 'rengongzhineng'
    # allowed_domains = ['n']

    # start_urls = ['http://ai.ailab.cn/?page=2']

    # rules = (
    #     Rule(LinkExtractor(allow='http://ai.ailab.cn/?page=\d+'),callback='parse_item'),
    # )
    def start_requests(self):
        cookies = {'UM_distinctid': '165e150703e2fb-08af887c8c9be5-37664109-100200-165e150703f222',
                   'nRhl_ba1e_saltkey': 't48vm82E',
                   'nRhl_ba1e_lastvisit': '1543477378',
                   'nRhl_ba1e_lastrequest': 'ac59KEGCexa9a4hg2m2EDyJpf%2BVF%2BezSEv3Bato7jQAA2vhW9arU',
                   'nRhl_ba1e_lastact': '1543557736%09index.php%09',
                   'CNZZDATA3202821': 'cnzz_eid%3D1503976435-1537078420-http%253A%252F%252Fwww.ailab.cn%252F%26ntime%3D1543557124',

                   }
        headers={
            'Referer': 'http://ai.ailab.cn/',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }
        for i in range(1,3):
            url='http://ai.ailab.cn/?page='+str(i)+''
            yield scrapy.Request(url,cookies=cookies,headers=headers,callback=self.parse)
    def parse(self, response):
        title=response.xpath("//ul[@class='list_jc']/li[2]/a[@class='title']/text()").extract()
        time=response.xpath("//li/p[@class='xx']/span[@class='click']").extract()
        print(time)
