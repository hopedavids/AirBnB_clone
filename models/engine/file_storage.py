#!/usr/bin/python3

import json
import os
import sys
sys.path.append('../')
from models.base_model import BaseModel


class FileStorage(BaseModel):
    def __init__(self):
        super().__init__(*args, **kwargs)
        self.__file_path = os.path.dirname(os.path)
        self.__objects = __dict__.super().__name__.id

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects.append(obj)
        return obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        if self.__file_path:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
            return self.__objects
    