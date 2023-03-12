#!/usr/bin/python3
"""Review class module that inherits from Basemodel
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """class Review inherits BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""

