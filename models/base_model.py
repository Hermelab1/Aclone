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
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timeformat)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel"""
        selfs = self.__class__.__name__
        return "[{}] ({}) {}".format(selfs, self.id, self.__dict__)

    def save(self):
        """Update updated_at with current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation of BaseModel"""
        dic_copy = self.__dict__.copy()
        dic_copy["__class__"] = self.__class__.__name__
        dic_copy['updated_at'] = self.updated_at.isoformat()
        dic_copy['created_at'] = self.created_at.isoformat()
        return dic_copy
