# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from content_aggregator.content_scraper.content_scraper.models import db_connect, create_table, Post
from content_aggregator.content_frontend import db
from content_aggregator.content_frontend.models import Post
# from content_aggregator.content_scraper.content_scraper.models import Post


class SiteScraperPipeline:
    def process_item(self, item, spider):
        return item


class OriginalSavePostsPipeline:
    def __init__(self):

        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        post = Post()
        post.source = item['post_source']
        post.title = item['post_title']
        post.date_posted = item['post_date']
        post.link = item['post_link']


        try:
            db.session.add(post)
            db.session.commit()

        except:
            db.session.rollback()
            raise

        finally:
            db.session.close()

        return item


class SavePostsPipeline:
    # def __init__(self):

        # engine = db_connect()
        # create_table(engine)
        # self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        # session = self.Session()
        source = item['post_source']
        title = item['post_title']
        date = item['post_date']
        link = item['post_link']
        post = Post(source=source, title=title, date_posted=date, link=link)


        try:
            db.session.add(post)
            db.session.commit()

        except:
            db.session.rollback()
            raise

        finally:
            db.session.close()

        return item