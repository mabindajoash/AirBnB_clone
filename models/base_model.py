#!/usr/bin/python3
"""
Module containing BaseModel class
"""


from datetime import datetime
import uuid
import models


class BaseModel:
    """defines all common attributes and methods for other classes"""
    def __init__(self, *args, **kwargs):
        """class constructer"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    value = datetime.fromisoformat(value)
                    setattr(self, key, value)
                    continue
                if key == 'updated_at':
                    value = datetime.fromisoformat(value)
                    setattr(self, key, value)
                    continue
                if key == '__class__':
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)


    def __str__(self):
        """string rep of an object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update date"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return dictionary with key/ value of __dict__"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        created_at = self.created_at.isoformat()
        updated_at = self.updated_at.isoformat()
        dict_copy['created_at'] = created_at
        dict_copy['updated_at'] = updated_at
        return dict_copy

