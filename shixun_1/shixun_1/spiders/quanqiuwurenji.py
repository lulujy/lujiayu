# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from ..items import Shixun1Item
class UavSpider(CrawlSpider):
    name = 'uav'
    # allowed_domains = ['m']
    start_urls = ['http://www.81uav.cn/uav-news/4.html']
    rules = (
        Rule(LinkExtractor(allow="http://www.81uav.cn/uav-news/4_\d+.html", ), follow=True),
        Rule(LinkExtractor(allow="http://www.81uav.cn/uav-news/\d{6}/\d{2}/\d+.html", restrict_css="div.news_left a"),callback="parse_item", follow=False),
    )
    def parse_item(self, response):
        # 标题
        sel = Selector(response)
        if sel.xpath("//h1/text()").extract_first():
            title = sel.xpath("//h1/text()").extract_first()
            print(title)
        else:
            title = ''
            print(response.url)
        #     来源
        if sel.xpath("//div[@class='view']/div[@class='info']/text()").extract()[-2]:
            laiyuan=sel.xpath("//div[@class='view']/div[@class='info']/text()").extract()[-2]
            print(laiyuan)
        else:
            raise Exception('laiyuan null')
        # 时间
        if sel.xpath("//div[@class='view']/div[@class='info']").re('\d{4}-\d{2}-\d{2}'):
            time = sel.xpath("//div[@class='view']/div[@class='info']").re('\d{4}-\d{2}-\d{2}')
        else:
            time = ''
        print(time)
        # 图片
        if sel.xpath("//div[@id='article']/p[2]/img/@src").extract():
            img=sel.xpath("//div[@id='article']/p[2]/img/@src").extract()
            print(img)
        else:
            img=''
        #     正文
        if sel.xpath("//div[@id='article']/p/text()").extract():
            content = sel.xpath("//div[@id='article']/p/text()").extract()
        else:
            content=''
        items = Shixun1Item()
        items['title'] = title
        items['laiyuan'] = laiyuan
        items['time'] = time
        items['img'] = img
        items['content'] = content

        return items
