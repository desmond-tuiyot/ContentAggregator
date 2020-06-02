# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from site_scraper.models import db_connect, create_table, Post
    # Quote, Author, Tag


class SiteScraperPipeline:
    def process_item(self, item, spider):
        return item


class SavePostsPipeline:
    def __init__(self):

        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        post = Post()
        post.source = item['post_source']
        post.title = item['post_title']
        post.date = item['post_date']
        post.link = item['post_link']

        try:
            session.add(post)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item

#
# class SaveQuotesPipeline(object):
#     def __init__(self):
#         """
#         Initializes database connection and sessionmaker
#         Creates tables
#         """
#         engine = db_connect()
#         create_table(engine)
#         self.Session = sessionmaker(bind=engine)
#
#
#     def process_item(self, item, spider):
#         """Save quotes in the database
#         This method is called for every item pipeline component
#         """
#         session = self.Session()
#         quote = Quote()
#         author = Author()
#         tag = Tag()
#         author.name = item["author_name"]
#         author.birthday = item["author_birthday"]
#         author.bornlocation = item["author_bornlocation"]
#         author.bio = item["author_bio"]
#         quote.quote_content = item["quote_content"]
#
#         # check whether the author exists
#         exist_author = session.query(Author).filter_by(name = author.name).first()
#         if exist_author is not None:  # the current author exists
#             quote.author = exist_author
#         else:
#             quote.author = author
#
#         # check whether the current quote has tags or not
#         if "tags" in item:
#             for tag_name in item["tags"]:
#                 tag = Tag(name=tag_name)
#                 # check whether the current tag already exists in the database
#                 exist_tag = session.query(Tag).filter_by(name = tag.name).first()
#                 if exist_tag is not None:  # the current tag exists
#                     tag = exist_tag
#                 quote.tags.append(tag)
#
#         try:
#             session.add(quote)
#             session.commit()
#
#         except:
#             session.rollback()
#             raise
#
#         finally:
#             session.close()
#
#         return item