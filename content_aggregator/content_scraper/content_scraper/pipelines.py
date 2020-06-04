# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# from sqlalchemy.orm import sessionmaker
# from scrapy.exceptions import DropItem
# from content_aggregator.content_scraper.content_scraper.models import db_connect, create_table
# from content_aggregator.content_frontend import db
# from content_aggregator.content_frontend.models import Post, Source
# from content_aggregator.content_scraper.content_scraper.models import Source, Post, session
from content_scraper.models import Source, Post, session


class ContentScraperPipeline:
    def process_item(self, item, spider):
        return item


class SavePostsPipeline:
    def __init__(self):
        # db.drop_all()
        # db.create_all()
        # session = session
        pass

    def process_item(self, item, spider):
        post = Post()
        post.title = item['post_title']
        post.link = item['post_link']
        post.date = item['post_date']
        # post = Post(title=title, link=link, date=date_posted)
        # source = Source(source_name=source_name, link=source_link)

        existing_source = session.query(Source).filter_by(source_name=item['post_source']).first()
        if existing_source is not None:  # the current source exists
            post.source = existing_source
        else:
            source = Source()
            source.source_name = item['post_source']
            source.link = item['post_source_link']
            post.source = source

        try:
            session.add(post)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item