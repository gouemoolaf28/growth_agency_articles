import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ArticlesSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['maddyness.com']
    start_urls = ['http://www.maddyness.com/?s=MaddyMoney/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=(
            "(//div[@class='home-article-card-wrapper']//a)[1]")), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for article in response.xpath("//a[@class='financement-link']"):
            yield {
                "company_name": article.xpath(".//div[@class='finance-card-company']/text()").get(),
                "site_url": article.xpath("./@href").get()
            }
