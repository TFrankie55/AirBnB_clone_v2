#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Integer, Float
from sqlalchemy.orm import relationship

from models.review import Review


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

        def reviews(self):
            """ Gets a list of all cities in state """
            return [reviews for reviews in models.storage.all(Review).values() if
                    self.id == reviews.place_id]

    # cities = relationship("City", back_populates="places")
