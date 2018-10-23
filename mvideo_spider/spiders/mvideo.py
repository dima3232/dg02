# -*- coding: utf-8 -*-
import scrapy
import json
import re


class MvideoSpider(scrapy.Spider):
    name = 'mvideo'
    allowed_domains = ['mvideo.ru']
    start_urls = ['https://www.mvideo.ru/televizory-i-cifrovoe-tv/televizory-65/f/category=4k-uhd-televizory-1682',
'https://www.mvideo.ru/televizory-i-cifrovoe-tv/televizory-65/f/tehnologiya_smart_tv=da',
'https://www.mvideo.ru/televizory-i-cifrovoe-tv/televizory-65/f/kvantovij_tochki_tv=da',
'https://www.mvideo.ru/televizory-i-cifrovoe-tv/televizory-65/f/category=oled-televizory-1987',
'https://www.mvideo.ru/televizory-i-cifrovoe-tv/televizory-65/f/izognut_ekran=da',
'https://www.mvideo.ru/televizory-i-cifrovoe-tv/televizory-65/f/razreshenie_ekrana_telev=full-hd',
'https://www.mvideo.ru/televizory-i-cifrovoe-tv/televizory-65/f/category=zhk-led-televizory-990',
'https://www.mvideo.ru/sputnikovoe-cifrovoe-tv/komplekty-sputnikovogo-tv-133']

    def parse(self, response):
        data = response.css('.sel-product-tile-title::attr(data-product-info)').extract()
        for item in data:
            yield json.loads(item)
