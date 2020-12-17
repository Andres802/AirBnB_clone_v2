#!/usr/bin/python3
""" Data Base Engine module """
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class DBStorage:
    """Class DBSTORAGE"""
    __engine = None
    __session = None

    def __init__(self):
        """ init method """
        env = os.getenv("HBNB_ENV")
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ return the dictionary with all class objects """
        clsdict = {}
        if cls is None:
            classes = [State, City]
            for clselement in classes:
                cls_query = self.__session.query(clselement).all()
        else:
            cls_query = self.__session.query(cls).all()
        for obj in cls_query:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            clsdict[key] = dic_query
        return clsdict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload objects from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                        expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ method used for sesssion closing """
        self.__session.close()
