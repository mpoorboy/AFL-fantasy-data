# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AflItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    player = scrapy.Field()
    position = scrapy.Field()
    start_price = scrapy.Field()
    current_price = scrapy.Field()
    own = scrapy.Field()
    games = scrapy.Field()
    be = scrapy.Field()
    round_1 = scrapy.Field()
    round_2 = scrapy.Field()
    round_3 = scrapy.Field()
    round_4 = scrapy.Field()
    round_5 = scrapy.Field()
    round_6 = scrapy.Field()
    round_7 = scrapy.Field()
    round_8 = scrapy.Field()
    round_9 = scrapy.Field()
    round_10 = scrapy.Field()
    round_11 = scrapy.Field()
    #round_12 = scrapy.Field()
    #pass
