#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from models import storage_type

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models. It defines all the
    universal attributes and methods for classes inheriting
    from it"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    try:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    except ValueError:
                        pass
                setattr(self, key, value)

            if 'id' not in kwargs:
                setattr(self, 'id', str(uuid.uuid4()))



    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """creates dictionary of the class and returns
        Return:
        returns a dictionary of all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        # Removing '_sa_instance_state' if it exists
        my_dict.pop('_sa_instance_state', None)

        return my_dict

    def delete(self):
        """Method that deletes the current instance from the storage
        by calling the delete method"""

        from models import storage
        storage.delete(self)
