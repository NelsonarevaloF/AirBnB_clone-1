#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all,delete')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            Return the list of City objects from storage linked to the current State
            """
            list_city = {}
            dictionary = models.storage.all(City)
            for key, value in dictionary.items():
                    if self.id == value.state_id:
                        list_city[key] = value
            return list_city.values()
