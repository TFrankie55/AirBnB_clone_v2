#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME, null
from sqlalchemy.orm import relationship

from models.city import City



class State(BaseModel, Base):
    """ State class """
    print("before createing state")
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", order_by=City.id ,back_populates="state", cascade="all, delete-orphan")