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


def parse_date(date):
    # if type(date) == list:
    #     date = ' '.join(date)
    date = date.split(' ')
    parsed = ""
    extract = True
    for word in date:
        if ':' in word and ('pm' in word or 'am' in word):
            extract = False
        elif not extract:
            continue
        if word == ',' or word == 'at':
            continue
        parsed = parsed + ' ' + word
    return parsed


def convert_datetime(date):
    # print("\n\n\n\n\n")
    print(date)
    # print("\n\n\n\n\n")
    try:
        return dateutil.parser.parse(date)
    except:
        return dateutil.parser.parse(parse_date(date))


class PostItem(Item):
    post_source = Field(
        output_processor=TakeFirst()
    )
    post_source_link = Field(
        output_processor=TakeFirst()
    )

    post_title = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    post_link = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    post_date = Field(
        input_processor=MapCompose(convert_datetime),
        output_processor=TakeFirst()
    )
