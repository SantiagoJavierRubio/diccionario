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
    start_urls = ['https://gameanswers.net/es/codycross-respuestas/']

    def parse(self, response):
        categorias = response.css('ul.level_list').xpath('li/a/@href').getall()
        for categoria in categorias:
            next_link = 'https://gameanswers.net/'+categoria
            yield Request(next_link, callback=self.parseCategory)

    def parseCategory(self, response):
        fases = response.css('ul.level_list').xpath('li/a/@href').getall()
        for fase in fases:
            next_link = 'https://gameanswers.net/'+fase
            yield Request(next_link, callback=self.parsePuzzles)

    def parsePuzzles(self, response):
        puzzles = response.css('div.row').xpath('div/p/a/@href').getall()
        for puzzle in puzzles:
            next_link = 'https://gameanswers.net/'+puzzle
            yield Request(next_link, callback=self.parseWords)

    def parseWords(self, response):
        definicion = response.css('div.row').xpath('h3/text()').get()
        palabra = response.css('div.row').xpath('p/strong/text()').get()
        if len(palabra)< 10:
            item = DiccionarioItem()
            item['palabra'] = palabra
            item['definicion'] = definicion
            yield item