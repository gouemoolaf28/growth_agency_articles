# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import gspread
import sqlite3


# class MaddynessPipeline:

#     collection_name = "articles"
#     gc = gspread.service_account(filename='./creds.json')

#     def open_spider(self, spider):
#         logging.warning("SPIDER OPENED FROM PIPELINE")
#         sh = self.gc.open('scrapetosheets').sheet1

#     def close_spider(self, spider):
#         logging.warning("SPIDER CLOSED FROM PIPELINE")

#     def process_item(self, item, spider):
#         sh.append_rows(item)
#         return item

class SQLitePipeline(object):

    def open_spider(self, spider):
        self.connection = sqlite3.connect("growthagency.db")
        self.c = self.connection.cursor()
        try:
            self.c.execute('''
                CREATE TABLE article(
                    company_name TEXT,
                    site_url TEXT
                )
            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO article (company_name, site_url) VALUES (?,?)
        ''', (
            item.get('company_name'),
            item.get('site_url')
        ))
        self.connection.commit()
        return item
