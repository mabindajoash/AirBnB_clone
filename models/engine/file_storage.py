#!/usr/bin/python3
"""
A module containing class 'File Storage'
"""


from models.base_model import BaseModel
import os
import json
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class FileStorage:
    """Serializes and deserializes instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets objects in __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes objects to json file"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump({key: obj.to_dict() for key, obj in FileStorage.__objects.items()}, f)

    def reload(self):
        """deserialize Json file"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                try:
                    data  =  json.load(f)
                    for key, value in data.items():
                        classname = value['__class__']
                        del value['__class__']
                        class_ = globals()[classname]
                        FileStorage.__objects[key] = class_(**value)
                except json.JSONDecodeError:
                    pass
