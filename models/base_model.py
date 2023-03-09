#!/usr/bin/python3
"""
This serves as the BaseModel, it contains the BaseModel class
and its' functions
"""
import json
import uuid
from datetime import datetime
import models
time_format = "%Y-%m-%dT%H:M:%S.%f"

class BaseModel:
    """Base class for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel class
        id: string - assigned with an uuis when an instance is created
        created_at: datetime - assign with the current datetime
        updated_at: datetime - update timestamp everytime object changes
        """

        if kwargs:
            self.__dict__ = kwargs
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs.get("created_at"),
                                                    time_format)
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs.get("updated_at"),
                                                    time_format)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)


    def save(self):
        """updates updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the an instance
        and the class name in the key __class__
        """
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = type(self).__name__
        for key, value in model_dict.items():
            if isinstance(value, datetime):
                model_dict[key] = value.strftime(time_format)
        return model_dict

    def __str__(self):
        """Print BAseModel info
        private method
        __str__: should print: [<class name>] (<self.if>) <self.__dict__>
        """
        return ("[{0}] ({1}) {2}".format(self.__class__.__name__,
                                        self.id, self.__dict__))
