# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HockeyTeamItem(scrapy.Item):
    # define the fields for your item here like:
    Team_Name = scrapy.Field()
    Year = scrapy.Field()
    Wins = scrapy.Field()
    Losses = scrapy.Field()
    OT_losses = scrapy.Field()
    Goal_for = scrapy.Field()
    Goal_against = scrapy.Field()
