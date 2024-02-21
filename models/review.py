#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    place_id = Column(ForeignKey("places.id"),String(60), nullable=False,)
    user_id = Column(ForeignKey("users.id"), String(60), nullable=False)
    text = Column(String(1024), nullable=False)
