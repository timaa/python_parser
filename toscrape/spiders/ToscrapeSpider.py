# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from toscrape.items import ToscrapeItem

ROOT_URL = "http://books.toscrape.com/catalogue/"


class ToscrapespiderSpider(scrapy.Spider):
    name = 'ToscrapeSpider'
    allowed_domains = ['books.toscrape.com']
    start_urls = []
    for i in range(1, 51):
        start_urls.append('http://books.toscrape.com/catalogue/page-{:d}.html'.format(i))

    def parse(self, response):
        root = Selector(response)
        hrefs = root.xpath('//article[@class="product_pod"]//h3/a/@href').extract()
        for href in hrefs:
            url = ROOT_URL + href
            yield scrapy.Request(url, callback=self.parse_book)

    def parse_book(self, response):
        root = Selector(response)
        item = ToscrapeItem()
        item['title'] = root.xpath('//div[@class="col-sm-6 product_main"]/h1/text()').extract()
        item['category'] = root.xpath('//ul[@class="breadcrumb"]/li/a/text()').extract()[2]
        item['price'] = root.xpath('//div[@class="col-sm-6 product_main"]/p[@class="price_color"]/text()').extract()
        item['rating'] = root.xpath('//div[@class="col-sm-6 product_main"]/p[@class="star-rating Three"]/@class').extract()
        item['available'] = root.xpath('//table[@class="table table-striped"]//tr[6]/td/text()').extract()
        item['priceExcludeTax'] = root.xpath('//table[@class="table table-striped"]//tr[3]/td/text()').extract()
        item['priceIncludeTax'] = root.xpath('//table[@class="table table-striped"]//tr[4]/td/text()').extract()
        yield item
