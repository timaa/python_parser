# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

class ToscrapePipeline(object):
    def process_item(self, item, spider):
        # item['title'] = root.xpath('//div[@class="col-sm-6 product_main"]/h1/text()').extract()
        # item['category'] = root.xpath('//ul[@class="breadcrumb"]/li/a/text()').extract()[2]
        # item['price'] = root.xpath('//div[@class="col-sm-6 product_main"]/p[@class="price_color"]/text()').extract()
        # item['rating'] = root.xpath(
        #     '//div[@class="col-sm-6 product_main"]/p[@class="star-rating Three"]/@class').extract()
        item['available'] = re.findall(r'[^\d]*([\d]+)[^\d]*', item['available'][0])[0]
        item['price'] = re.findall(r'([0-9.]+)', item['price'][0])[0]
        item['priceExcludeTax'] = re.findall(r'([0-9.]+)', item['priceExcludeTax'][0])[0]
        item['priceIncludeTax'] = re.findall(r'([0-9.]+)', item['priceIncludeTax'][0])[0]
        # item['priceIncludeTax'] = root.xpath('//table[@class="table table-striped"]//tr[4]/td/text()').extract()
        return item
