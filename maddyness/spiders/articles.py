import scrapy
from scrapy.loader import ItemLoader
from ..items import MaddynessItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ArticlesSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['maddyness.com']
    start_urls = ['http://www.maddyness.com/?s=MaddyMoney/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=(
            "(//div[@class='home-article-card-wrapper']//a)")), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # article_item = MaddynessItem()
        for article in response.xpath("//a[@class='financement-link']"):
            loader = ItemLoader(item=MaddynessItem(),
                                selector=article, response=response)
            loader.add_xpath(
                "company_name", ".//div[@class='finance-card-company']/text()")
            loader.add_xpath("site_url", ".//@href")

            yield loader.load_item()

            # article_item['company_name'] = article.xpath(
            #     ".//div[@class='finance-card-company']/text()").get()
            # article_item['site_url'] = article.xpath("./@href").get()
            # yield article_item
