# -*- coding: utf-8 -*-
import scrapy

from newsSpider.items import NewsspiderItem

class YaowenspiderSpider(scrapy.Spider):
    name = 'yaowenSpider'
    allowed_domains = ['gdqy.edu.cn']
    start_urls = ['https://www.gdqy.edu.cn/info/1057/7101.htm']

    def parse(self, response):
        item = NewsspiderItem()
        # 提取数据
        item['title'] = response.xpath('/html/body/div[2]/div/form/div[1]/div[1]').extract()
        item['content'] = response.xpath('/html/body/div[2]/div/form/div[1]/div[2]').extract()
        yield item
