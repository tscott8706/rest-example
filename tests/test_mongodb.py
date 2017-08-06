from flask import Flask
from unittest import TestCase
from restexample.mongodb import MongoDB

class TestMongoDB(TestCase):

    def tearDown(self):
        MongoDB.set_mongodb(None)

    def test_get_db_before_create_raises_exception(self):
        self.assertRaises(RuntimeError, MongoDB.get_mongodb)

    def test_get_db_after_create(self):
        fake_mongo = "abc"
        MongoDB.set_mongodb(fake_mongo)
        self.assertEqual(MongoDB.get_mongodb(), fake_mongo)
