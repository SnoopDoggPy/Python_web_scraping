# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import  MongoClient


class BookparserPipeline:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.mongo_base = self.client.Books

    def process_item(self, item, spider):
        if item["price_new"]:
            item["price_new"] = int(item["price_new"].replace('р.', '').replace(' ', ''))

        if item["price_old"]:
            item["price_old"] = int(item["price_old"].replace('р.', '').replace(' ', ''))

        if item["rate"]:
            item["rate"] = float(item["rate"].replace(',', '.'))

        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item

    def __del__(self):
        self.client.close()


