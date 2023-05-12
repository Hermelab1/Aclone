#!/usr/bin/python3

class Storage:
    def __init__(self):
        """initializes the storage layer"""
        pass

    def save(self, model):
        """save the given model to the storage layer"""
        pass
    def get(self, model_class, id):
        """Retrives a model of the given class and id from the storage layer"""
        pass

    """create a singleton instance of the storage layer"""
storage = Storage()   
