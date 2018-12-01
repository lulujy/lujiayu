# -*- coding: utf-8 -*-
import scrapy


class WangSpider(scrapy.Spider):
    name = 'wang'
    # allowed_domains = ['f']
    start_urls = ['https://www.doutula.com/photo/list/']

    def parse(self, response):
        for i in range(1,50):
            imgg=response.xpath("//div/a[@class='col-xs-6 col-sm-3']/img[@class='img-responsive lazy image_dta']/@src").extract()
