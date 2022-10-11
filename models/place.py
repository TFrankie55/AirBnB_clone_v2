#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self)
        self.__dict__.update(kwargs)
