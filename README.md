# Analyzing_world_cuisines
In this repository I share my end-to-end project. Scraping data, analyzing data, fitting a model, evaluating a model.

## Scraping data

I built a web-scraper using the Scrapy library (more robust solutions than BeautifulSoup) to get recipes from each cuisine listed on [https://www.bbc.co.uk/food/cuisines](BBC Food). I chose BBC due to the perceived quality and availability. Other webpages like Allrecipes are quite chaotic, allow user-entered recipes which in turn may influence data quality (e.g. poorly labeled cuisines, inconsistency). 

With my scraper, I collected:

- Recipe name
- Cook time
- Prep time
- Average rating
- Number of ratings
- Recipe list (just ingredients)
- Full recipe list (including amount)
- Cuisine

I scraped over 2k recipes and will further do an EDA & ML.

## EDA

-tbd

## Machine Learning and Predictive Modelling

-tbd
