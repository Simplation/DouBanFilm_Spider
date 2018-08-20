# -*- coding: utf-8 -*-

import scrapy

from douban.douban_spider.items import DoubanSpiderItem


class DemoSpider(scrapy.Spider):
    # 爬虫的名称
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 起始的 URL
    start_urls = ['https://movie.douban.com/top250']

    # scrapy 默认的解析方法， response：解析结果
    def parse(self, response):
        # 解析第一页的数据
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']//li")
        for i_item in movie_list:

            # 实例化 Item 对象
            douban_item = DoubanSpiderItem()

            # 设置并获取详细的数据
            douban_item['serial_number'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name'] = i_item.xpath(
                ".//div[@class='info']//div[@class='hd']/a/span[1]/text()").extract_first()
            content = i_item.xpath(".//div[@class='info']//div[@class='bd']//p[1]/text()").extract()

            # 遇到多行数 据需要进行字符串的处理
            for i_content in content:
                content_s = "".join(i_content.split())
                douban_item['instruce'] = content_s
            douban_item['start'] = i_item.xpath(".//div[@class='info']//div[@class='bd']//span["
                                                "@class='rating_num']/text()").extract_first()

            douban_item['evaluate'] = i_item.xpath(".//div[@class='item']//div[@class='info']//div["
                                                   "@class='bd']//span[4]/text()").extract_first()

            douban_item['describe'] = i_item.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//p["
                                                   "@class='quote']/span[1]/text()").extract_first()

            # 将数据给 piplines
            yield douban_item

        # 添加剩余条目规则, 使用 xpath 添加 next 链接
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link, callback=self.parse)
