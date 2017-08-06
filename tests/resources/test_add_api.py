from flask import Flask
from restexample.resources.add_api import add_resources
from unittest import TestCase

class TestAddApi(TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.testing = True

    def test_add_resources_adds_uris_to_api(self):
        add_resources(self.app)
        routes = [rule.rule for rule in self.app.url_map.iter_rules()]
        self.assertTrue("/person" in routes)
