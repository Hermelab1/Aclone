#!/usr/bin/python3
"""review class module"""


from models.base_model import BaseModel


class Review(BaseModel):
    """review class detail"""
    place_id = ""
    user_id = ""
    text = ""
