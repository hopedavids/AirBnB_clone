#!/usr/bin/python3
"""
This module contains the User class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ This is the user class that inherits from the BaseModel Attribute """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    # def __init__(self, email, password, first_name, last_name):
    #     super().__init__(self, *args, **kwargs)
    #     self.email = email
    #     self.password = password
    #     self.first_name = first_name
    #     self.last_name = last_name