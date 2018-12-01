# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    # allowed_domains = ['m']
    # start_urls = ['http://m/']
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    def start_requests(self):
        zixun=input('请输入资讯:...')
        url='https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word='+str(zixun)
        yield scrapy.Request(url,self.parse,headers=self.headers)
    def parse(self, response):
        lianjie=response.xpath("//div/h3/a/@href").extract()
        for i in lianjie:
            print(i)
            yield scrapy.Request(url=i,callback=self.parse_er,headers=self.headers)
    def parse_er(self,response):
        if response.xpath("//div[@class='article-title']/h2/text()").extract():
            title=response.xpath("//div[@class='article-title']/h2/text()").extract()
            print(title)
        else:
            raise Exception
        if response.xpath('//*[@id="article"]/div[2]/div[2]/div/span[2]/text()').extract():
            time=response.xpath('//*[@id="article"]/div[2]/div[2]/div/span[2]/text()').extract()
            print(time)
        else:
            raise Exception
        if response.xpath('//*[@id="article"]/div[2]/div[2]/p/text()').extract():
            zuozhe=response.xpath('//*[@id="article"]/div[2]/div[2]/p/text()').extract()
            print(zuozhe)
        else:
            raise Exception
        if response.xpath("//div[@class='article-content']/p/span[@class='bjh-p']/text()").extract():
            content=response.xpath("//div[@class='article-content']/p/span[@class='bjh-p']/text()").extract()
            print(content)
        else:
            raise Exception

        if response.xpath("//div[@class='img-container'][1]/img[@class='large']/@src/text()").extract():
            img=response.xpath("//div[@class='img-container'][1]/img[@class='large']/@src/text()").extract()
            print(img)
        else:
            raise Exception