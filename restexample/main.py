from flask import Flask
from flask_pymongo import PyMongo
from restexample.mongodb import MongoDB
from restexample.resources.add_api import add_resources

def create_app():
    return Flask("restexample")

def main():
    app = create_app()
    app.config["MONGO_HOST"] = "192.168.1.2"
    add_resources(app)
    MongoDB.set_mongodb(PyMongo(app))
    app.run(host="0.0.0.0", port=5000)
