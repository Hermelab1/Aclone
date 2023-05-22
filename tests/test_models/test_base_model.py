#!/usr/bin/python 3
import unittest
import models
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """A class to define unittest for BaseModel"""
    def setUp(self):
        self.bm = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.bm.id, str)
        self.assertIsInstance(self.bm.created_at, datetime)
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_save(self):
        old_updated_at = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(old_updated_at, self.bm.updated_at)

    def test_to_dict(self):
        dict_copy = self.bm.to_dict()
        bm_created = self.bm.created_at()
        bm_updated = self.bm.updated_at()
        self.assertIsInstance(dict_copy, dict)
        self.assertEqual(dict_copy['__class__'], 'BaseModel')
        self.assertEqual(dict_copy['id'], self.bm.id)
        self.assertEqual(dict_copy['created_at'], bm_created.isoformat())
        self.assertEqual(dict_copy['updated_at'], bm_updated.isoformat())


if __name__ == '__main__':
    unittest.main()
