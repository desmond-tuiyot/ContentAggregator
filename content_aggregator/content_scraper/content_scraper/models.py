from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os

engine = create_engine('sqlite:///C:\\Users\\NyneTray\\Documents\\Computer_Science\\Python\\ContentAggregator\\content_aggregator\\content_frontend\\content.db', echo=True)
# engine = create_engine('postgres://cdpsefgabpblxg:cbf62189bbd895a92260e2c54dd92324a35c5fcafc204b662d8f95e4999c907d@ec2-52-202-146-43.compute-1.amazonaws.com:5432/d4hb0bqnaoorsg')
Base = declarative_base(engine)


########################################################################
class Post(Base):
    """"""
    __tablename__ = 'post'
    __table_args__ = {'autoload': True}
    source_id = Column(Integer, ForeignKey('source.id'), nullable=False)


class Source(Base):
    """"""
    __tablename__ = 'source'
    __table_args__ = {'autoload': True}
    posts = relationship('Post', backref='source', lazy=True)



# ----------------------------------------------------------------------
def loadSession():
    """"""
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


session = loadSession()
# if __name__ == "__main__":
#     session = loadSession()
#     res = session.query(Bookmarks).all()
#     print
#     res[1].title
