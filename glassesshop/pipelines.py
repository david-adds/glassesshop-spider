# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from typing import Collection
# from itemadapter import ItemAdapter
# import logging
# import pymongo


# class MongodbPipeline:
#     collection_name = "glasses"
        
#     def open_spider(self,spider):
#         self.client =  pymongo.MongoClient("mongodb+srv://david_adds:1234@cluster0.tyndb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")    
#         self.db = self.client["glassesshop"]
        
#     def close_spider(self,spider):
#         self.client.close()
            
#     def process_item(self, item, spider):
#         self.db[self.collection_name].insert(item)
#         return item
import sqlite3

class SQLlitePipeline(object):
        
    def open_spider(self,spider):
        self.connection = sqlite3.connect('glassesshop.db')
        self.c = self.connection.cursor()
        self.c.execute(''' 
                       CREATE TABLE glasses(
                            url TEXT,
                            image_url TEXT,
                            product_name TEXT,
                            price TEXT
                       )
                       '''
                       )
        self.connection.commit()
        
    def close_spider(self,spider):
        self.client.close()
            
    def process_item(self, item, spider):

        self.c.execute(''' 
                       INSERT INTO glasses (url,image_url,product_name,price) VALUES(?,?,?,?)
                       ''', (
                           item.get('url'),
                           item.get('image_url'),
                           item.get('product_name'),
                           item.get('price')
                       )
        )
        self.connection.commit()
        return item
