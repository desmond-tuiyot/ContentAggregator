from scrapy.crawler import CrawlerProcess

from content_aggregator.content_scraper.content_scraper.spiders.posts_spider import AnalyticsVidhyaSpider, CrazyProgrammerSpider


def main():
    process = CrawlerProcess()
    process.crawl(AnalyticsVidhyaSpider)
    process.crawl(CrazyProgrammerSpider)
    process.start()
