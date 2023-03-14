#!/usr/bin/python3

import uuid
from datetime import datetime
import sys
from engine.file_storage import FileStorage


class BaseModel:
    '''This is the base model class object for all attributes
        will be used by the airbnb application
    '''

    def __init__(self, *args, **kwargs):
        # The initializer method for the BaseModel class
        if kwargs:  # updating the attributes of the base model
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()
            self.__dict__.update(kwargs)
            models.storage.new(self)


    def __str__(self):
        ''' The __str__ method for the BaseModel class which
        turn to translate the the attribute name into a string
        '''
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) ({self.created_at})]"

    def save(self):
        '''The save method for the BaseModel class which determines
        if the object needs to be saved or not
        '''
        self.updated_at = datetime.now().isoformat()
        models.storage.save()

    def to_dict(self):
        ''' The to_dict method that converts the attributes to
        a dictionary
        '''
        obj_dict = self.__dict__
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at
        obj_dict['updated_at'] = self.updated_at
        return obj_dict
