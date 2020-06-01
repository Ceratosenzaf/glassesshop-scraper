# -*- coding: utf-8 -*-
import scrapy


class BestSellersSpider(scrapy.Spider):
    name = 'best_sellers'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers/']

    def parse(self, response):
        glasses = response.xpath('//div[contains(@class, "m-p-product")]')
        for item in glasses:
            yield{
                'url': item.xpath(".//div[@class='pimg default-image-front']/a/@href").get(),
                'img_url': item.xpath(".//div[@class='pimg default-image-front']/a/img[1]/@src").get(),
                'name': item.xpath(".//div[@class='row']/p[contains(@class, 'pname')]/a/text()").get(),
            }
