#!/usr/bin/python3
"""Defination of a classes"""
import models
import uuid 
from datetime import datetime


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args,  **kwargs):
        """
        Initialize instance attributes
        *kwargs a key value pairs of attributes
        *args it is unused
        """
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, timeformat)
                else:
                    self.__dict__[i] = j

    def __str__(self):
        """Return string representation of BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation of BaseModel"""
        dic_copy = self.__dict__.copy()
        dic_copy['created_at'] = self.created_at.isoformat()
        dic_copy['updated_at'] = self.updated_at.isoformat()
        dic_copy["__class__"] = self.__class__.__name__
        return dic_copy
