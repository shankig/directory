from flask import Flask
from flask.ext import restful
from flask.ext.mongoengine import MongoEngine
from resource import DirectoryResource, DirectoryUpdateResource


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": "app_directory"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
api = restful.Api(app)

api.add_resource(DirectoryResource, '/')
api.add_resource(DirectoryUpdateResource, '/<directory_key>')

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()