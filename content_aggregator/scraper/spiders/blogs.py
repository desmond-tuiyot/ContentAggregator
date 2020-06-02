import scrapy
from scrapy.crawler import CrawlerProcess
import csv


class AnalyticsVidhyaSpider(scrapy.Spider):
    name = 'analytics_vidhya'
    start_urls = ['https://www.analyticsvidhya.com/blog-archive/page/1',
                 ]

    def parse(self, response):
        articles = response.css('.post-box-oblog')
        dates = articles.css('.entry-date::attr(datetime)').getall()
        titles = articles.css('.entry-title').xpath('./a/@title').getall()
        links = articles.css('.entry-title').xpath('./a/@href').getall()
        data = list(zip(dates, titles, links))

        with open('data.csv', mode='a', newline='') as data_file:
            data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for post in data:
                data_writer.writerow(post)

        for a in response.css('div.pagination a.number.current + a'):
            yield response.follow(a, callback=self.parse)



def main():
    process = CrawlerProcess()
    process.crawl(AnalyticsVidhyaSpider)
    process.start()


if __name__ == "__main__":
    main()
