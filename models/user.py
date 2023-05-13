#!/usr/bin/python3
"""Defination of user class"""
from model.base_model import BaseModel


class User(BaseModel):
    """Represenation of user
    email, Password, Firstname, Last Name"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
