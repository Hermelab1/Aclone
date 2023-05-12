import json
import os.path


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__object[key] = obj

    def save(self):
        with open(FileStorage.__file_path, mode="w", encoding="utf-8")as file:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, file)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as file:
                objs = json.load(file)
                for obj in objs.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
