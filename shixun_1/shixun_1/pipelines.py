# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
class Shixun1Pipeline(object):
    def process_item(self, item, spider):
        self.myclinet=pymongo.MongoClient()
        self.mydb=self.myclinet['tech']
        self.col=self.mydb['te']
        title=item['title']
        laiyuan=item['laiyuan']
        time=item['time']
        img=item['img']
        content=item['content']
        # daodu=item['daodu']
        self.col.insert({'标题':title,'来源':laiyuan,'时间':time,'图片':img,'正文':content})
        return item
