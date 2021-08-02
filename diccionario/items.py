# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DiccionarioItem(scrapy.Item):
    palabra = scrapy.Field()
    definicion = scrapy.Field()
