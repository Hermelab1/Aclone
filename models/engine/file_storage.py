#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """A class to define file storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary objects"""
        return self.__objects

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
            with open(self.__file_path) as f:
                jload = json.load(f).items()
                obdic = {k: BaseModel(**v) for k, v in jload}
        except FileNotFoundError:
            pass
