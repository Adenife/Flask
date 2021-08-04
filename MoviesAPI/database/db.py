# import the mongo engine
from flask_mongoengine import MongoEngine

# create an object of the class MongoEngine
db = MongoEngine()


# function to initialize the database. this will be called in the main py file
def initialize_db(app):
    db.init_app(app)