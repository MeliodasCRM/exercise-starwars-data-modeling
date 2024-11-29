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
    username = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    character_favorites = relationship('Favourite_Characters', back_populates='user')
    vehicle_favorites = relationship('Favourite_Vehicles', back_populates='user')
    planet_favorites = relationship('Favourite_Planets', back_populates='user')

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    specie = Column(String(250), nullable=False)

    character_favorites = relationship('Favourite_Characters', back_populates='character')

class Vehicles(Base):
    __tablename__='vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)

    vehicle_favorites = relationship('Favourite_Vehicles', back_populates='vehicle')

class Planets(Base):
    __tablename__='planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)

    planet_favorites = relationship('Favourite_Planets', back_populates='planet')

class Favourite_Characters(Base):
    __tablename__ = 'favourite_characters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    character = relationship('Characters', back_populates='character_favorites')
    user = relationship('User', back_populates='character_favorites')

class Favourite_Planets(Base):
    __tablename__ = 'favourite_planets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    planet = relationship('Planets', back_populates='planet_favorites')
    user = relationship('User', back_populates='planet_favorites')

class Favourite_Vehicles(Base):
    __tablename__ = 'favourite_vehicles'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    vehicle = relationship('Vehicles', back_populates='vehicle_favorites')
    user = relationship('User', back_populates='vehicle_favorites')

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
