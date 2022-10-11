#!/usr/bin/python3
""" State Module for HBNB project """
from unicodedata import name
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self)
        self.name = kwargs.get("name", "")
