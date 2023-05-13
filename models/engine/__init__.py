#!/usr/bin/python3
"""Defines the storage class"""


import json


class FileStorage:
    """serializes an instance to JSON and
    deserializes back to instance"""

    __objects = {}

    __file_path = "file.json"
    def all(self, cls=None):
        """Returns a dictionary of __objects"""
        return self.__objects
    def new(self, obj):
        if obj is not None:
            key = obj._class__.__name+"."+obj.id
            self._objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON File"""
    j_obj = {}
    for key in self.__objects:
        j_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(j_obj, f)

    def reload(self):
        """Deserializes the JSON file to objects"""
        try:
            with open(FileStorage>__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except:
            pass 
