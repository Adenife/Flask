from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail


app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
mail = Mail(app)

from resource.routes import initialize_routes


# initialize your database
initialize_db(app)
# initialize routes
initialize_routes(api)