#!/usr/bin/python3
"""a class user that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """user class detail"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
