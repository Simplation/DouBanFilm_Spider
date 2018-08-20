# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
from douban.douban_spider.settings import mysql_host, db_user, db_password, db_name
import pymysql


class DoubanSpiderPipeline(object):

    def __init__(self):
        self.host = mysql_host
        self.user = db_user
        self.dbpwd = db_password
        self.dbname = db_name

    def process_item(self, item, spider):
        # """
        # 保存 csv 文件
        # 获取当前工作目录
        base_dir = os.getcwd()
        fiename = base_dir + '/douban_data.csv'
        # 从内存以追加的方式打开文件，并写入对应的数据
        with open(fiename, 'a') as f:
            f.write(item['serial_number'] + '\n')
            f.write(item['movie_name'] + '\n')
            f.write(item['instruce'] + '\n')
            f.write(item['start'] + '\n')
            f.write(item['evaluate'] + '\n')
            f.write(item['describe'] + '\n\n')
        # """

        """
        # 插入数据库
        data = dict(item)

        # db = pymysql.connect(hosr=self.host,
        #                      user=self.user,
        #                      password=self.dbpwd,
        #                      db=self.dbname)
        db = pymysql.Connect(host='localhost',
                             user='root',
                             password='wangzhao',
                             db='test',
                             charset='utf8')

        # sql 语句
        sql = 'insert into test.douban (`serial_number`, `movie_name`, `instruce`, `start`, `evaluate`, `describe`) values (%s, %s, %s, %s, %s, %s)'

        # 获取 cursor 对象
        cursor = db.cursor()
        try:
            values = (data['serial_number'], data['movie_name'], data['instruce'], data['start'], data['evaluate'],
                      data['describe'])
            cursor.execute(sql, values)
            db.commit()
        except BaseException as e:
            db.rollback()
            print(e)

        finally:
            # 关闭游标和数据库
            cursor.close()
            db.close()
        """

        return item
