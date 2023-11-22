#!/usr/bin/python3
""" City Module for HBNB project """

from models import storage_type
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', cascade='all, delete', backref='cities')

    else:
        state_id = ""
        name = ""
