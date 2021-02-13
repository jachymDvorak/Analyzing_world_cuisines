# Analyzing_world_cuisines
In this repository I share my end-to-end project. Scraping data, analyzing data, fitting a model, evaluating a model.

## Scraping data

I built a web-scraper using the Scrapy library (more robust solutions than BeautifulSoup) to get recipes from each cuisine listed on [BBC Food](https://www.bbc.co.uk/food/cuisines). I chose BBC due to the perceived quality and availability. Other webpages like Allrecipes are quite chaotic, allow user-entered recipes which in turn may influence data quality (e.g. poorly labeled cuisines, inconsistency). 

Note the scraper has to be run with a command in cmd from the project folder (obviously output can be JSON etc.)

```
scrapy crawl recipe_spider -o BBC_recipe_data.csv
```

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

- Most used ingredients in each cuisine.

![10 world cuisines](https://github.com/jachymDvorak/Analyzing_world_cuisines/blob/main/cuisine_plots.png?raw=true)

## Machine Learning and Predictive Modelling

-tbd
