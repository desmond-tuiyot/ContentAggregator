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


class DataScienceCentralSpider(scrapy.Spider):
    name = 'data_science_central'
    start_urls = ['https://www.datasciencecentral.com/profiles/blog/list',
                ]

    def parse(self, response):
        articles = response.css('div.xg_blog_list div.xg_module_body')
        source = 'Data Science Central'
        source_link = 'https://www.datasciencecentral.com/profiles/blog/list'
        for article in articles:
            loader = ItemLoader(item=PostItem(), selector=article)
            loader.add_value('post_source', source)
            loader.add_value('post_source_link', source_link)
            loader.add_css('post_title', 'h3.title a::text')
            loader.add_css('post_link', 'h3.title > a::attr(href)')
            date = self.valid_date(article.css('p.small::text').getall())
            loader.add_value('post_date', date)
            post_item = loader.load_item()
            yield post_item

        for a in response.css('ul.pagination a[class]'):
            yield response.follow(a, callback=self.parse)

    def valid_date(self, p_s):
        MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']

        for phrase in p_s:
            words = phrase.split()
            for word in words:
                if word in MONTHS:
                    return phrase.strip()


class StackAbuseSpider(scrapy.Spider):
    name = 'stack_abuse'
    start_urls = ['https://stackabuse.com/',
                ]

    def parse(self, response):
        articles = response.css('div.col-md-8 article.post')
        source = 'Stack Abuse'
        source_link = 'https://stackabuse.com'
        for article in articles:
            loader = ItemLoader(item=PostItem(), selector=article)
            loader.add_value('post_source', source)
            loader.add_value('post_source_link', source_link)
            loader.add_css('post_title', 'div.post-head h2.post-title a::text')
            post_link = source_link + article.css('div.post-head h2.post-title a::attr(href)').get()
            loader.add_value('post_link', post_link)
            loader.add_css('post_date', 'div.post-meta span.date::text')
            post_item = loader.load_item()
            yield post_item

        for a in response.css('nav.pagination a.older-posts'):
            yield response.follow(a, callback=self.parse)


class MachineLearningMasterySpider(scrapy.Spider):
    name = 'machine_learning_mastery'
    start_urls = ['https://machinelearningmastery.com/blog/',
                ]

    def parse(self, response):
        articles = response.css('section#main article')
        source = 'Machine Learning Mastery'
        source_link = 'https://machinelearningmastery.com/blog/'
        for article in articles:
            loader = ItemLoader(item=PostItem(), selector=article)
            loader.add_value('post_source', source)
            loader.add_value('post_source_link', source_link)
            loader.add_css('post_title', 'header h2.entry-title a::text')
            loader.add_css('post_link', 'header h2.entry-title a::attr(href)')
            loader.add_css('post_date', 'div.post-meta abbr.date::attr(title)')
            post_item = loader.load_item()
            yield post_item

        for a in response.css('div.pagination a.next::attr(href)'):
            yield response.follow(a, callback=self.parse)


class LazyProgrammerSpider(scrapy.Spider):
    name = 'lazy_programmer'
    start_urls = ['https://lazyprogrammer.me/',
                ]

    def parse(self, response):
        articles = response.css('div.container div.row div.col-xs-12 div.post-title')
        dates = response.css('div.container div.row div.col-xs-12 div.post-body')
        source = 'Lazy Programmer'
        source_link = 'https://lazyprogrammer.me/'
        for i, article in enumerate(articles):
            loader = ItemLoader(item=PostItem(), selector=article)
            loader.add_value('post_source', source)
            loader.add_value('post_source_link', source_link)
            loader.add_css('post_title', 'h1 a::text')
            loader.add_css('post_link', 'h1 a::attr(href)')
            date = dates[i]
            loader.add_value('post_date', date.css('p::text').get())
            post_item = loader.load_item()
            yield post_item

        for a in response.css('div.post-body div.row div.col-xs-6 a::attr(href)'):
            yield response.follow(a, callback=self.parse)


class CodePenSpider(scrapy.Spider):
    name = 'codepen'
    start_urls = ['https://blog.codepen.io/',
                ]

    def parse(self, response):
        articles = response.css('div.page-wrap section.article')
        source = 'CodePen Blog'
        source_link = 'https://blog.codepen.io/'
        for article in articles:
            loader = ItemLoader(item=PostItem(), selector=article)
            loader.add_value('post_source', source)
            loader.add_value('post_source_link', source_link)
            loader.add_css('post_title', 'h1 a::text')
            loader.add_css('post_link', 'h1 a::attr(href)')
            loader.add_css('post_date', 'time.block-time::text')
            post_item = loader.load_item()
            yield post_item

        for a in response.css('div.older-posts a::attr(href)'):
            yield response.follow(a, callback=self.parse)
