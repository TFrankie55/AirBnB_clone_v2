#!/usr/bin/python3
"""
create DBStorage
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()


class DBStorage:
    __engine: None
    __session: None

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{db}", pool_pre_ping=True, echo=True)
        
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls != None:
            rows = self.__session.query(cls).all()
            return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in
                rows}
        else:
            c = [City, Amenity, User, State, Place, Review]
            objects = []
            for k in c:
                objects += self.__session.query(k)
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in
                objects}


    def new(self, obj):
        print(obj)
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()
