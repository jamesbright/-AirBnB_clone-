#!/user/bin/python3
"""module contains user class that inherits BaseModel class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits BaseModel class
    """

    email = ""
    password = ""
    firs_name = ""
    last_name = ""
