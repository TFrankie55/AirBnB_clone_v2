#!/usr/bin/python3
""" Place Module for HBNB project """

from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Integer, Float, Table
from sqlalchemy.orm import relationship

from models.review import Review

place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", backref="place",
                               secondary=place_amenity, viewonly=False)
    else:
        @property
        def reviews(self):
            """ Gets a list of all cities in state """
            return [reviews for reviews in models.storage.all(Review).values() if
                    self.id == reviews.place_id]
        
        @property
        def amenities(self):
            """ Gets a list of all cities in state """
            from models.amenity import Amenity
            return [amenities for amenities in models.storage.all(Amenity).values() if
                    self.id == amenities.place_id]
        
        @amenities.setter
        def amenities(self, obj):
            if obj.__name__ == "Amenity":
                print(obj)


    # cities = relationship("City", back_populates="places")
