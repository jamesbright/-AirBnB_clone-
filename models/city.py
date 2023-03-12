#!/usr/bin/python3
"""City class module that ingerits from Basemodel
"""
from models.base_model import BaseModel

class City(BaseModel):
    """class City inherits BaseModel
    """
    state_id = ""
    name = ""
