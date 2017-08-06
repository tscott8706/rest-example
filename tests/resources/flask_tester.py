from flask import Flask
from flask_restful import Api
from unittest import mock

class TestResource(object):

    URI = "/test"

    def __init__(self, resource):
        app = Flask(__name__)
        app.testing = True
        self.test_client = app.test_client()
        api = Api(app)
        api.add_resource(resource, self.URI)
        self.mongo_patch = mock.patch(resource.__module__ + ".MongoDB")

    def get(self):
        self.test_client.get(self.URI)

    def post(self, data):
        self.test_client.post(self.URI, data=data)

    def start_mocking_mongo(self):
        self.mock_db = self.mock_mongo = self.mongo_patch.start()

    def stop_mocking_mongo(self):
        self.mongo_patch.stop()
