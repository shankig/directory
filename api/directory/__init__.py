from flask import Flask
from flask.ext import restful
from flask.ext.mongoengine import MongoEngine
from resource import DirectoryResource, DirectoryUpdateResource

#App conf
app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": "app_directory"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
api = restful.Api(app)

#db connection
db = MongoEngine(app)

#Api urls
api.add_resource(DirectoryResource, '/')
api.add_resource(DirectoryUpdateResource, '/<directory_key>') # directory_key is pincode

if __name__ == '__main__':
    app.run()