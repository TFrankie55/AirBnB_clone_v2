#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self)
        self.__dict__.update(kwargs)
