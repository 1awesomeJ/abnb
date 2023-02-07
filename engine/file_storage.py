#!/usr/bin/python3
"""This module handles the file storage class"""


from models.base_model import BaseModel
import json
    

class FileStorage:
    """This class handles the storage engine capabilities"""
    __file_path = "storage.json"
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
        k = json.dumps(FileStorage.__objects)
        with open (FileStorage._file_path, "w") as my_file:
            my_file.write(k)

    def reload(self):
        """This deserializes a JSON file to objects"""
        try:
            with open(FileStorage.__filepath) as my_file:
                FileStorage_objects = json.loads(FileStorage.__filepath)
        except FileNotFoundError:
            exit(2)
