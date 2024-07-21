import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    email = Column(String(150), nullable=False)
    login = Column(String(100), nullable =False)
class Vehicles (Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    max_velocity = Column(String(250), nullable=False)
    model = Column(String(150), nullable=False)
    capacity = Column(String(20), nullable =False)

class Starships (Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    max_velocity = Column(String(250), nullable=False)
    model = Column(String(150), nullable=False)
    capacity = Column(String(20), nullable =False)

class Species (Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    origin = Column(String(250), nullable=False)
    classification = Column(String(150), nullable=False)
    language = Column(String(20), nullable =False)

class Fav (Base):
    __tablename__ = 'fav'
    id = Column(Integer, primary_key=True)
    


# class Person(Base):
#     __tablename__ = 'person'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
