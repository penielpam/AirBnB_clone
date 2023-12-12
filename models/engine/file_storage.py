#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def get_all_objects(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def add_new_object(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save_objects_to_file(self):
        """Serialize __objects to the JSON file __file_path."""
        objects_dict = FileStorage.__objects
        serialized_objects = {obj_key: objects_dict[obj_key].to_dict()
                              for obj_key in objects_dict.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def load_objects_from_file(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                serialized_objects = json.load(file)
                for serialized_obj in serialized_objects.values():
                    class_name = serialized_obj["__class__"]
                    del serialized_obj["__class__"]
                    self.add_new_object(eval(class_name)(**serialized_obj))
        except FileNotFoundError:
            return
