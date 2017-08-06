from flask_restful import Api
from restexample.resources.person import Person

def add_resources(app):
    api = Api(app)
    api.add_resource(Person, "/person")
