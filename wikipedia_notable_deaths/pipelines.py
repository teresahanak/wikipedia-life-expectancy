# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import logging
import sqlite3

# class WikipediaNotableDeathsPipeline:
#     def open_spider(self, spider):
#         logging.warning('Spider Opened -- Pipeline')
#
#     def close_spider(self, spider):
#         logging.warning('Spider Closed -- Pipeline')
#
#     def process_item(self, item, spider):
#         return item
#
class SQLitePipeline:

    def open_spider(self, spider):
        # create database file
        self.connection = sqlite3.connect('refs5.db')
        # we need a cursor object to execute SQL queries
        self.c = self.connection.cursor()
        #  try/except will help when running this for the +2nd time (we can't create the same table twice)
        try:
            # query: create table with columns
            self.c.execute('''
                CREATE TABLE refs5(
                    link TEXT,
                    num_references TEXT
                )
            ''')
            # save changes
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        # query: insert data into table
        self.c.execute('''
            INSERT INTO refs5 (link, num_references) VALUES(?,?)
        ''', (
            item.get('link'),
            item.get('num_references')
        ))
        # save changes
        self.connection.commit()
        return item