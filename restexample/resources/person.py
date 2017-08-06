from flask_restful import reqparse, Resource
from restexample.mongodb import MongoDB

class Person(Resource):

    get_parser = reqparse.RequestParser()
    get_parser.add_argument("name", type=str, help="Name of person")

    post_parser = reqparse.RequestParser()
    post_parser.add_argument("name", type=str, help="Name of person")
    post_parser.add_argument("birthdate", type=str, help="Birthday in MM/DD/YYYY format")

    def get(self):
        args = self.get_parser.parse_args()
        name = args["name"]

        if name is None:
            cursor = MongoDB.get_mongodb().db.person.find({})
            return {"/" + person["name"]: person["birthdate"] for person in cursor}
        else:
            person = MongoDB.get_mongodb().db.person.find_one({"name":name})
            return {"/" + person["name"]: person["birthdate"]}

    def post(self):
        args = self.post_parser.parse_args()
        #raise RuntimeError(MongoDB.get_mongodb().db)
        MongoDB.get_mongodb().db.person.insert(args)
