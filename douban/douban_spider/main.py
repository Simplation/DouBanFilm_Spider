#!/usr/bin/env python
# encoding: utf-8
"""
@file: main.py
@time: 2018-08-16 10:17
@desc: 程序运行入口
"""

from scrapy import cmdline

cmdline.execute('scrapy crawl douban_spider'.split())
