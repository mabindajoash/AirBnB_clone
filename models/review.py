#!/usr/bin/python3
"""
Module containing class Review
"""


from models.basemodel import BaseModel
import models

class Review(BaseModel):
   """class Review"""
    place_id = ""
    user_id = ""
    text = ""
