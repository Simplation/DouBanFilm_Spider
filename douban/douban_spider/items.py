# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    """ 定义需要爬取的内容 """

    # 序号
    serial_number = scrapy.Field()
    # 名称
    movie_name = scrapy.Field()
    # 介绍
    instruce = scrapy.Field()
    # 星级
    start = scrapy.Field()
    # 评论
    evaluate = scrapy.Field()
    # 描述
    describe = scrapy.Field()
