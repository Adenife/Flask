# import the mongo engine
from flask_mongoengine import MongoEngine
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_user import UserMixin

# create an object of the class MongoEngine
db = MongoEngine()


# function to initialize the database. this will be called in the main py file
def initialize_db(app):
    db.init_app(app)

def get_user(user_id):
    user = User.objects(id=user_id).first()
    return user

class User(db.Document, UserMixin):
    username = db.StringField(required=True, min_length=6)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    def hash_password(self):
        self.password = generate_password_hash(self.password). decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])