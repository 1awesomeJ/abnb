#!/usr/bin/env python3
"""
A script that defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
	""" defines all common attributes/methods for other classes """
	def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
	if len(kwargs) != 0:
		for key, value in kwargs.items():
			if key == "created_at" or key == "updated_at":
				self.__dict__[key] = datetime.strptime(value, time_format)
			else:
				self.__dict__[key] = value
	else:
		models.storage.new(self)

	def __str__(self):
		cls_str = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
	return (cls_str)

	def save(self):
		"""This method updates the public instance attribute updated_at with the current datetime"""
		self.updated_at = datetime.today()
		models.storage.save()

	def to_dict(self):
		"""This method returns a dictionary containing all keys/values of __dict__ of the instance"""
		ret_dict = self.__dict__.copy()
		ret_dict["created_at"] = self.created_at.isoformat()
		ret_dict["updated_at"] = self.updated_at.isoformat()
		ret_dict["__class__"] = self.__class__.__name__
		return ret_dict
