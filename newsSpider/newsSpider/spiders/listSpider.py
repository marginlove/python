# -*- coding: utf-8 -*-
import scrapy

from newsSpider.items import NewsspiderItem


class ListspiderSpider(scrapy.Spider):
    name = 'listSpider'
    allowed_domains = ['gdqy.edu.cn']
    start_urls = ['https://www.gdqy.edu.cn/gqxw1/yw.htm']

    def parse(self, response):
        item['title'] = response.xpath('/html/body/div[2]/div/form/div[1]/div[1]').extract()
        item['content'] = response.xpath('/html/body/div[2]/div/form/div[1]/div[2]').extract()
        pass
