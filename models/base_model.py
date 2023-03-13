#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        self.__dict__.update(kwargs)

    def __str__(self):
        class_name = type(self).__name__
        return f"[{class_name}]{self.id}={self.created_at}]"

    def save(self):
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        obj_dict = self.__dict__
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at
        obj_dict['updated_at'] = self.updated_at
        return obj_dict
