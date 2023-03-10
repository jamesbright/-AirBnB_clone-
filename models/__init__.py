#!/usr/bin/python3
"""Linking classes between files
"""
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()

classes = {
        "BaseModel": BaseModel,
        "User": User
        }
