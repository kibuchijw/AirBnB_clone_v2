#!/usr/bin/python3
""" State Module for HBNB project """

import models
from os import getenv
from models.city import City
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """

    __tablename = 'states'

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')

    else:
        @property
        def cities(self):
            """Method capturing a list of all related City Objects"""
            cityList = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    cityList.append(city)

            return cityList
