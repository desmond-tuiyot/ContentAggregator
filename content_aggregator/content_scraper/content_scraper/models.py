from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    source = Column('source', Text())
    title = Column('title', Text())
    link = Column('link', Text())
    date_posted = Column('date', DateTime)