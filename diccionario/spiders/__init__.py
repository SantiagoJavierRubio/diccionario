# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
import unidecode
from diccionario.items import DiccionarioItem
from scrapy.http import Request

class DiccionarioSpider(scrapy.Spider):
    name = 'diccionario'
    start_urls = ['https://juegocodycross.com/crucero/grupo-650-fase-4']

    def parse(self, response):
        palabras = response.css('p.respuesta strong::text').getall()
        definiciones = response.css('h2.pregunta::text').getall()
        next_link = response.xpath('//a[contains(@rel, "next")]/@href').get()
        def_list = []
        i=0
        for palabra in palabras:
            if len(palabra)< 10:
                item = DiccionarioItem()
                item['palabra'] = palabra
                item['definicion'] = definiciones[i]
                i+=1
                yield item
            else: i+1
        yield Request(next_link, callback=self.parse)