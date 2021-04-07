import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Follower(Base):
    __tablename__ = 'Follower'
    id = Column(Integer, primary_key=True)
    User_to_id = Column(Integer, ForeignKey('User.id'))
    User_from_id = Column(Integer, ForeignKey('User.id'))

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('User.id'))

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    Type = Column(Integer)
    url = Column(String(250))
    Post_id= Column(Integer, ForeignKey('Post.id'))

class Coment(Base):
    __tablename__ = 'Coment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    Author_id= Column(Integer, ForeignKey('Post.id'))
    User_id = Column(Integer, ForeignKey('User.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')