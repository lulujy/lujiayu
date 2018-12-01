# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
import re
import json
from ..items import Shixun1Item
class Tech(CrawlSpider):
    name = 'tech'
    # allowed_domains = ['n']
    # start_urls = ['http://tech.163.com/']
    def start_requests(self):
        for i in range(1,5):
            url='http://tech.163.com/special/00097UHL/tech_datalist_0'+str(i)+'.js?callback=data_callback'
            yield scrapy.Request(url,self.parse_item)
    def parse_item(self, response):
        url_er = re.findall('"docurl":"(.*?)"', response.text)
#         for url in url_er:
#             yield scrapy.Request(url, self.parse)
#     def parse(self, response):
#         # 标题
#         if response.xpath("//div[@id='epContentLeft']/h1/text()").extract():
#             title=response.xpath("//title/text()").extract()
#             print(title)
#         else:
#             raise Exception('title null')
#         # 来源
#         if response.xpath("//div[@id='epContentLeft']/h1/text()").extract():
#             laiyuan=response.xpath('//*[@id="ne_article_source"]/text()').extract()
#             print(laiyuan)
#         else:
#             raise Exception('laiyuan null')
# #         时间
#         if response.xpath("//div[@id='epContentLeft']/h1/text()").extract():
#             time=response.xpath('//*[@id="epContentLeft"]/div[1]/text()').extract()
#             print(time)
#         else:
#             raise Exception('time null')
# #         图片
#         if response.xpath("//div[@id='endText']/p[@class='f_center']/img/@src").extract():
#             img=response.xpath("//div[@id='endText']/p[@class='f_center']/img/@src").extract()
#             print(img)
#         else:
#             img=''
#         #     正文
#         if response.xpath("//div[@id='endText']/p/text()").extract():
#             content=response.xpath("//div[@id='endText']/p/text()").extract()
#             print(content)
#         else:
#             content=''
#
# #         导读
#         if response.xpath("//div[@class='post_body']/div[@id='endText']/p[1]/text()").extract():
#             daodu =response.xpath("//div[@class='post_body']/div[@id='endText']/p[1]/text()").extract()
#             print(daodu)
#         else:
#             daodu=''
#
#         items=Shixun1Item()
#         items['title']=title
#         items['laiyuan']=laiyuan
#         items['time']=time
#         items['img']=img
#         items['content']=content
#         items['daodu']=daodu
#         yield items



