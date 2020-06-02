import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.loader import ItemLoader
from site_scraper.items import PostItem


post_item = PostItem()


class AnalyticsVidhyaSpider(scrapy.Spider):
    name = 'analytics_vidhya'
    start_urls = ['https://www.analyticsvidhya.com/blog-archive/page/1',
                 ]

    def parse(self, response):
        global post_item
        articles = response.css('.post-box-oblog')

        for article in articles:
            loader = ItemLoader(item=post_item, selector=article)
            loader.add_css('post_date', '.entry-date::attr(datetime)')
            loader.add_xpath('post_title', './h3[@class="entry-title"]/a/@title')
            loader.add_xpath('post_link', './h3[@class="entry-title"]/a/@href')
            post_item = loader.load_item()
            yield post_item

        for a in response.css('div.pagination a.number.current + a'):
            yield response.follow(a, callback=self.parse)


# def main():
#     process = CrawlerProcess()
#     process.crawl(AnalyticsVidhyaSpider)
#     process.start()
#
#
# if __name__ == "__main__":
#     main()
