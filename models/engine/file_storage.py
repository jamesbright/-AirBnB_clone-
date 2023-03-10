#!/usr/bin/python3
"""
saves object to a file
has methods that manipulate object saving and retrieval
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serializes objects to a JSON file
    and deserializes JSON file to objects
    """
    __file_path = "file.json"
    __objects = {}

    classes = {
        "BaseModel": BaseModel,
        "User": User
        }

    def all(self):
        """Returns all objects
        """
        return (FileStorage.__objects)


    def new(self, obj):
        """Sets __obj the obj with key
        <obj class name>.id
        """
        new_obj_id = "{}.{}".format(type(obj).__name__,
                                    obj.id)
        FileStorage.__objects[new_obj_id] = obj

    def save(self):
        """serializes __objects to JSON file
        """
        new_dict = {}
        for key in FileStorage.__objects.keys():
            new_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, mode="w",
                  encoding="UTF-8") as des_file:
            (json.dump(new_dict, des_file))

    def reload(self):
        """Deserializes the JSON file to __objects
        if the JSON file exists; otherwise, do nothing)
        """
        try:
            with open(FileStorage.__file_path, mode="r",
                    encoding="UTF-8") as src_file:
                for key, value in (json.load(src_file)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
