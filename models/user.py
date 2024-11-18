#!/usr/bin/python3
"""model containing class 'User'"""


import models.engine.file_storage
from models.base_model import BaseModel
import models


class User(BaseModel):
    """user class inheriting from MaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
