# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

# class StackoverflowPipeline(object):
#     def process_item(self, item, spider):
#         return item

"""
以下内容来自 settings.py
# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'stackoverflow.pipelines.StackoverflowPipeline': 300,
}
"""


#     StackoverflowPipeline
class StackoverflowPipeline(object):
    def __init__(self):
        # self.connection = pymongo.MongoClient('68.183.180.71', 27017)
        self.connection = pymongo.MongoClient('127.0.0.1', 27017)
        self.db = self.connection.scrapy
        self.collection = self.db.stackoverflow

    def process_item(self, item, spider):
        if not self.connection or not item:
            return
        self.collection.save(item)

    def __del__(self):
        if self.connection:
            self.connection.close()
