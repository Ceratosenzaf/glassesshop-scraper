# -*- coding: utf-8 -*-
import scrapy


class BestSellersSpider(scrapy.Spider):
    name = 'best_sellers'
    allowed_domains = ['www.glassesshop.com/bestsellers']
    start_urls = ['http://www.glassesshop.com/bestsellers/']

    def parse(self, response):
        pass
