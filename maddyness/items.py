# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class MaddynessItem(scrapy.Item):
    company_name = scrapy.Field(
        output_processor=TakeFirst()
    )
    site_url = scrapy.Field(
        output_processor=TakeFirst()
    )
