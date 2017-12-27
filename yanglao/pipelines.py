# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import pymysql

class YanglaoPipeline(object):
    def process_item(self, item, spider):
        return item
'''
class MysqlTwistedPipeline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls,settings):
        connect = pymysql.connect(
            host = settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            port = settings["MYSQL_PORT"],
            password = settings["MYSQL_password"],
            charset = "utf8"
        )
        con = connect.cursor()

'''


