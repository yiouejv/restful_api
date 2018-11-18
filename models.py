#encoding: utf-8
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from config import session as db_session, Base

# 用户
# 文章
# 标签


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(50))


article_tag = Table(
    'article_tag',
    Base.metadata,
    Column('article_id', Integer, ForeignKey('article.id'),primary_key=True),
    Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True)
)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(Text)
    author_id = Column(Integer, ForeignKey('user.id'))

    author = relationship('User', backref=backref('articles'))
    tags = relationship('Tag', backref=backref('articles'), secondary=article_tag)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))


Base.metadata.create_all()



