# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ToscrapeItem(scrapy.Item):
    category = scrapy.Field()
    title = scrapy.Field()
    rating = scrapy.Field()
    available = scrapy.Field()
    price = scrapy.Field()
    priceExcludeTax = scrapy.Field()
    priceIncludeTax = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
