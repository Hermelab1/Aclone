#!/usr/bin/python3
"""A class to difine a File Storage class"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Defination of abstract storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets object with key class"""
        objname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objname, obj.id)] = obj

    def save(self):
        """to serializes the obejectb to the json file"""
        objcdict = FileStorage.__objects
        obdict = {obj: objcdict[obj].to_dict() for obj in objcdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obdict, f)

    def reload(self):
        """to deserialize the json file to the object"""
        obdic = self.__objects
        try:
            with open(FileStorage.__file_path) as f:
                obdict = json.load(f)
                for o in obdict.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return
