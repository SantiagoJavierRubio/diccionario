# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
import unidecode
from diccionario.items import DiccionarioItem

class DiccionarioSpider(scrapy.Spider):
    name = 'diccionario'
    start_urls = ['http://www.culturageneral.net/palabrastecnicas/']

    def parse(self, response):
        palabras = response.xpath('//b/text()').getall()
        definiciones = response.xpath('//td/text()').getall()

        def_list = []

        for definicion in definiciones:
            text = ' '.join(definicion.split())
            if text == '':
                continue
            else:
                def_list.append(text)

        for palabra in palabras:
            if palabra == 'Palabra' or palabra == 'Definición':
                continue
            else:
                palabra = palabra.replace(' ', '')
                palabra = unidecode.unidecode(palabra)
                definicion_valida = def_list.pop(0)

                item = DiccionarioItem()
                item['palabra'] = palabra
                item['definicion'] = definicion_valida

                yield item