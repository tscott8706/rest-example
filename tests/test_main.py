from flask import Flask
from restexample.main import *
from unittest import mock, TestCase

class TestMain(TestCase):

    def test_create_app_creates_Flask_app(self):
        self.assertTrue(isinstance(create_app(), Flask))

    @mock.patch("restexample.main.create_app")
    @mock.patch("restexample.main.add_resources")
    @mock.patch("restexample.main.MongoDB")
    @mock.patch("restexample.main.PyMongo")
    def test_main_starts_app_on_port_5000(self, mock_pymongo, mock_db, mock_add_resources, mock_app):
        main()
        self.assertTrue(mock_add_resources.called)
        self.assertTrue(mock_db.set_mongodb.called)
        mock_app.return_value.run.assert_called_once_with(host="0.0.0.0", port=5000)
