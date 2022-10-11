#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self)
        self.__dict__.update(kwargs)
