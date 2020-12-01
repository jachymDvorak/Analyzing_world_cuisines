# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RecipeItem(scrapy.Item):
    name = scrapy.Field()
    prep_time = scrapy.Field()
    cook_time = scrapy.Field()
    servings = scrapy.Field()
    rating = scrapy.Field()
    rating_count = scrapy.Field()
    ingredients = scrapy.Field()
    cuisine = scrapy.Field()
    ingredients_full = scrapy.Field()

    