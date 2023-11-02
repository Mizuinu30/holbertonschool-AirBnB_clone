#!/usr/bin/python3
import unittest
from models.review import Review
import datetime
from models.base_model import BaseModel
from models import storage
"""
Unittest Module for Review class
"""


class TestUser(unittest.TestCase):
    ''' Unittest for Review class '''

    def setUp(self):
        self.review = Review()

    def test_object_Instantiation(self):
        ''' instantiates class '''
        self.review = Review()

    def testattr(self):
        ''' test Class: Review attributes '''
        self.review = Review()
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertFalse(hasattr(self.review, "random_attr"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertTrue(hasattr(self.review, "id"))
        self.assertEqual(self.review.text, "")
        self.assertEqual(self.review.__class__.__name__, "Review")

    def testsave(self):
        ''' testing method: save '''
        self.review = Review()
        self.review.save()
        self.assertTrue(hasattr(self.review, "updated_at"))

    def teststr(self):
        ''' testing __str__ return format of BaseModel '''
        self.review = Review()
        s = "[{}] ({}) {}".format(self.review.__class__.__name__,
                                  str(self.review.id), self.review.__dict__)
        self.assertEqual(print(s), print(self.review))

    def test_inheritance(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_methods(self):
        self.assertTrue(hasattr(Review, "save"))
        self.assertTrue(hasattr(Review, "to_dict"))

    def test_datetime_attributes(self):
        self.assertIsInstance(self.my_review.created_at, datetime)
        self.assertIsInstance(self.my_review.updated_at, datetime)

    def test_attribute_existence(self):
        self.assertTrue(hasattr(self.my_review, "place_id"))
        self.assertTrue(hasattr(self.my_review, "user_id"))
        self.assertTrue(hasattr(self.my_review, "text"))

    def test_save(self):
        old_updated_at = self.my_review.updated_at
        self.my_review.save()
        self.assertNotEqual(old_updated_at, self.my_review.updated_at)


if __name__ == '__main__':
    unittest.main()
