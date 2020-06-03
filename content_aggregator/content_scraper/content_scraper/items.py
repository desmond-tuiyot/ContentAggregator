# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from datetime import datetime
import dateutil.parser
import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst


def remove_quotes(text):
    # strip the unicode quotes
    text = text.strip(u'\u201c'u'\u201d')
    return text


def convert_date(text):
    # convert string March 14, 1879 to Python date
    return datetime.strptime(text, '%B %d, %Y')


def parse_location(text):
    # parse location "in Ulm, Germany"
    # this simply remove "in ", you can further parse city, state, country, etc.
    return text[3:]


class QuoteItem(Item):
    quote_content = Field(
        input_processor=MapCompose(remove_quotes),
        # TakeFirst return the first value not the whole list
        output_processor=TakeFirst()
        )
    author_name = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
        )
    author_birthday = Field(
        input_processor=MapCompose(convert_date),
        output_processor=TakeFirst()
    )
    author_bornlocation = Field(
        input_processor=MapCompose(parse_location),
        output_processor=TakeFirst()
    )
    author_bio = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
        )
    tags = Field()


def convert_datetime(date):
    return dateutil.parser.parse(date)


class PostItem(Item):
    post_source = Field(
        output_processor=TakeFirst()
    )
    post_title = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    post_date = Field(
        input_processor=MapCompose(convert_datetime),
        output_processor=TakeFirst()
    )
    post_link = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
