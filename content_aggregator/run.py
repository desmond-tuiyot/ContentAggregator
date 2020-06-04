# from scrapy.crawler import CrawlerProcess
from content_aggregator.content_frontend import app
# from content_aggregator.content_scraper.content_scraper.spiders import posts_spider

if __name__ == '__main__':
    # process = CrawlerProcess()
    # process.crawl(posts_spider.AnalyticsVidhyaSpider)
    # process.start()

    app.run(debug=True)
