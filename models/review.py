#!/usr/bin/python3
"""
Module containing class Review
"""


from models.basemodel import BaseModel


class Review(BaseModel):
   """class Review"""
    place_id = ""
    user_id = ""
    text = ""
