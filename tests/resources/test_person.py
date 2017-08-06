from restexample.resources.person import Person
from tests.resources.flask_tester import TestResource
from unittest import TestCase

class TestPerson(TestCase):

    def setUp(self):
        self.tester = TestResource(Person)
        self.tester.start_mocking_mongo()

    def tearDown(self):
        self.tester.stop_mocking_mongo()

    def test_post(self):
        self.tester.post({"name":"MyName", "birthdate":"01/02/2001"})

