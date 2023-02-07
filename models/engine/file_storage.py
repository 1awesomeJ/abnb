#!/usr/bin/python3
"""This module handles the file storage class"""


from models.base_model import BaseModel
import json


class FileStorage:
    """This class handles the storage engine capabilities"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method returns dictionary instantiated objects"""
        return FileStorage.__objects

    def new(self, obj):
        """This method sets object with key object class name"""
        oc_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(oc_name, obj.id)] = obj

    def save(self):
        """This serializes __objects to the JSON file (__file_path)"""
        odict = FileStorage.__objects
        obj_dict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as my_file:
            json.dump(obj_dict, my_file)

    def reload(self):
        """This deserializes a JSON file to objects"""
        try:
            with open(FileStorage.__file_path) as my_file:
                obj_dict = json.load(my_file)
                for ob in obj_dict.values():
                    cls_name = ob["__class__"]
                    del ob["__class__"]
       	except FileNotFoundError:
            return
