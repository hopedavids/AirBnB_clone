#!/usr/bin/python3

"""
This module creates an instance of the FileStorege class which interacts between the instances of the BaseModel class and the file.json file that contains the information of the created objects.
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
