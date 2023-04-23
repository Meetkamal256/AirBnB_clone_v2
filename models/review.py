#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from uuid import uuid4
import os

class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)
        setattr(self, "id", str(uuid4()))
        for i, j in kwargs.items():
            setattr(self, i, j)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'reviews'
        place_id =  Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""