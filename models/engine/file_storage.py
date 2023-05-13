import json
import os.path


class FileStorage:
    """Serialization and deserialization to and from JSON file."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__object[key] = obj

    def save(self):
        """Save the dictionary to the JSON file."""
        with open(FileStorage.__file_path, mode="w", encoding="utf-8")as file:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, file)

    def reload(self):
        """Load the dictionary from the JSON file."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as file:
                objs = json.load(file)
                for obj in objs.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
