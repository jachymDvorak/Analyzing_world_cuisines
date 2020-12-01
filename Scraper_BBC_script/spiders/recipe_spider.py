# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:43:44 2020

@author: Jáchym
"""

# go to all, then get all letters

import scrapy
import json
from recipes_cuisines.items import RecipeItem

class ItalianSpider(scrapy.Spider):
    
    name = "italian_spider"
    
    def start_requests(self):
        start_urls =  ['https://www.bbc.co.uk/food/cuisines']
        for url in start_urls:
            yield scrapy.Request(url = url, callback = self.parse_cuisines)
            
    def parse_cuisines(self, response):
        cuisine_cards = response.xpath('//a[contains(@class,"promo__cuisine")]/@href').extract()
        for url in cuisine_cards:
            yield response.follow(url = url, callback = self.parse_all_recipes)
            
    def parse_all_recipes(self, response):
        #all_recipes = response.xpath('//div[@class="see-all-recipes-link__container"]/a[class="see-all-recipes-link"]/@href').extract()
        all_recipes = response.css('div.food-body.gel-pica > div.food-grid.food-grid--full-width > div > div.see-all-recipes__wrap.gel-wrap > div > a::attr(href)')
        for url in all_recipes:
            yield response.follow(url = url, callback = self.parse_main)
    
    def parse_main(self, response):
        recipe_cards = response.xpath('//a[contains(@class,"main_course")]/@href').extract()
        for url in recipe_cards:
            yield response.follow(url = url, callback = self.parse_card)
        next_page = response.xpath('//div[@class="pagination gel-wrap"]/ul[@class="pagination__list"]/li[@class="pagination__list-item pagination__priority--0"]/a[@class="pagination__link gel-pica-bold"]/@href').get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            print(next_page_url)
            yield scrapy.Request(url = next_page_url, callback = self.parse_main)

    def parse_card(self, response):
        item = RecipeItem()
        recipe_raw = response.xpath('//script[@type="application/ld+json"][contains(., \'"@type":"Recipe"\')]/text()').get()
        recipe = json.loads(recipe_raw)
        recipe_rating = recipe['aggregateRating']
        item['cuisine'] = recipe['recipeCuisine']
        item['rating'] = recipe_rating['ratingValue']
        item['rating_count'] = recipe_rating['ratingCount']
        item['ingredients_full'] = recipe['recipeIngredient']
        item['name'] = response.xpath('//h1[contains(@class,"title__text")]/text()').extract()
        item['prep_time'] = response.xpath('//div[contains(@class,"recipe-metadata-wrap")]/p[@class="recipe-metadata__prep-time"]/text()').extract_first()
        item['cook_time'] = response.xpath('//p[contains(@class,"cook-time")]/text()').extract_first()
        item['servings'] = response.xpath('//p[contains(@class,"serving")]/text()').extract_first()
        item['ingredients'] = response.css('li.recipe-ingredients__list-item > a::text').extract()
        return item
