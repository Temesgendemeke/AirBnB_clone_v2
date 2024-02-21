#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    

class DBStorage:
    cities = relationship("City", back_populates="State",cascade="all, delete-orphan" )
    state = relationship("City", back_populates="City", cascade="all, delete-orphan")