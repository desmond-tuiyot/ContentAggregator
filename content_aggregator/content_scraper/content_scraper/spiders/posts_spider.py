import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.loader import ItemLoader
# from content_aggregator.content_scraper.content_scraper.items import PostItem
from content_scraper.items import PostItem
import json


class AnalyticsVidhyaSpider(scrapy.Spider):
    name = 'analytics_vidhya'
    start_urls = ['https://www.analyticsvidhya.com/blog-archive/page/1',
                ]

    def parse(self, response):
        articles = response.css('.post-box-oblog')
        source = 'Analytics Vidhya'
        source_link = 'https://www.analyticsvidhya.com/blog-archive'
        for article in articles:
            loader = ItemLoader(item=PostItem(), selector=article)
            loader.add_value('post_source', source)
            loader.add_value('post_source_link', source_link)
            loader.add_xpath('post_title', './h3[@class="entry-title"]/a/@title')
            loader.add_xpath('post_link', './h3[@class="entry-title"]/a/@href')
            loader.add_css('post_date', '.entry-date::attr(datetime)')
            post_item = loader.load_item()
            yield post_item

        for a in response.css('div.pagination a.number.current + a'):
            yield response.follow(a, callback=self.parse)


class CrazyProgrammerSpider(scrapy.Spider):
    name = 'crazy_programmer'
    start_urls = ['https://thecrazyprogrammer.com/page/1',
                ]

    def parse(self, response):
        # print("\n\n\nvisited page\n\n\n")
        articles = response.css('article header.entry-header h2.entry-title')
        source = 'The Crazy Programmer'
        source_link = 'https://thecrazyprogrammer.com'
        for article in articles:
            loader = ItemLoader(item=PostItem(), selector=article)
            loader.add_value('post_source', source)
            loader.add_value('post_source_link', source_link)
            loader.add_css('post_title', 'h2.entry-title a::text')
            loader.add_css('post_link', 'h2.entry-title a::attr(href)')

            post_item = loader.load_item()
            date_url = article.css('h2.entry-title a::attr(href)').get()

            yield response.follow(date_url, callback=self.parse_date, meta={'post_item': post_item})

        for a in response.css('nav#nav-below div.nav-previous a'):
            yield response.follow(a, callback=self.parse)


    def parse_date(self, response):
        post_item = response.meta['post_item']
        loader = ItemLoader(item=post_item, selector=response)
        script_data = response.css('script.yoast-schema-graph::text').get()
        converted = json.loads(script_data)
        parts = converted['@graph']
        date = None
        for part in parts:
            if 'datePublished' in part:
                date = part['datePublished']
                break
        loader.add_value('post_date', date)
        yield loader.load_item()

# def main():
#     process = CrawlerProcess()
#     process.crawl(AnalyticsVidhyaSpider)
#     process.start()
#
#
# if __name__ == "__main__":
#     main()
