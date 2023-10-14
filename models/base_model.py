#!/usr/bin/python3
"""Base class Module
Defines all common attributes/methods for other classes
"""

import uuid
from models import storage
from datetime import datetime


class BaseModel:

    """Base model class"""

    def __str__(self):
        """Returns a string representation
        of an instance in a readable way."""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        return my_dict
