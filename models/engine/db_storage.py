#!/usr/bin/python3
"""Defines the DBStorage engine."""
from os import getenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize DBStorage instance.
        Create engine linked to MySQL database using environment variables.
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)

        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def all(self, cls=None):
        """
        Query objects based on class name.

        Args:
            cls (str): Class name to query. Defaults to None.

        Returns:
            list: List of objects based on class name.
        """
        from models import base_model

        all_objects = {}

        if cls:
            if hasattr(base_model, cls):
                all_objects[cls] = self.__session.query(getattr(base_model, cls)).all()
        else:
            for table in Base.metadata.tables:
                class_name = table.capitalize()
                if hasattr(base_model, class_name):
                    all_objects[class_name] = self.__session.query(getattr(base_model, class_name)).all()

        return all_objects

    def new(self, obj):
        """
        Add object to the session.

        Args:
            obj (obj): Object to be added to the session.
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit changes to the session."""
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete object from the session.

        Args:
            obj (obj): Object to be deleted from the session. Defaults to None.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create tables and session."""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
