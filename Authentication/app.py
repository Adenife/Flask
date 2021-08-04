from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_login import login_user, logout_user, current_user, LoginManager
from database.data import User, LoginForm, RegisterForm, initialize_db, db, get_user
from flask_bcrypt import Bcrypt
from flask_user import login_required, UserManager

app = Flask(__name__)

bootstrap = Bootstrap(app)
app.config.from_envvar('ENV_FILE_LOCATION')
bcrypt = Bcrypt(app)
initialize_db(app)
user_manager = UserManager(app, db, User)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # username = request.form.get("username")
        # password = request.form.get("password")
        user = User.objects(username=username).first()
        authorized = user.check_password(password=password)
        if not authorized:
            return '<h1>Invalid username or password</h1>'
        
        login_user(user, remember=form.remember.data)
        return redirect(url_for('dashboard'))


    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        user.hash_password()
        user.save()

        return '<h1>New user has been created!</h1>'

    return render_template('signup.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)