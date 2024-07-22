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
    password = Column(String(100), nullable =False)
    favorites = relationship("Favorite", back_populates="user")

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    max_velocity = Column(String(250), nullable=False)
    model = Column(String(150), nullable=False)
    capacity = Column(String(20), nullable =False)
    favorites = relationship("Favorite", back_populates="vehicle")

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    max_velocity = Column(String(250), nullable=False)
    model = Column(String(150), nullable=False)
    capacity = Column(String(20), nullable =False)
    favorites = relationship("Favorite", back_populates="starship")

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    origin = Column(String(250), nullable=False)
    classification = Column(String(150), nullable=False)
    language = Column(String(20), nullable =False)
    favorites = relationship("Favorite", back_populates="species")

class Fav (Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    fav_vehicle = Column(Integer, ForeignKey('vehicle.id'))
    fav_starships = Column(String, ForeignKey('starship.id'))
    fav_species = Column(Integer, ForeignKey('species.id'))

    user = relationship("User", back_populates="fav")
    vehicles = relationship(Vehicle)
    starships = relationship(Starship)
    species = relationship(Species)
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
