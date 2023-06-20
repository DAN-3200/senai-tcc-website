from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

# Definições de App ----------------------------------------------------------
app = Flask(__name__)

# -- Vincular ao banco
usuario_db = "root" ; senha_db = "1234" ; banco_db = "bank"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{usuario_db}:{senha_db}@localhost:3306/{banco_db}'
app.app_context().push()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ab44d789595b66efeda6b633e686a9db'

# Instâncias -------

# -- Database(Flask-SQLAlchemy)
db = SQLAlchemy(app)

# -- Migrate(Flask-Migrate)
migrate = Migrate(app, db)

# -- Flask-Login
lm = LoginManager()
lm.login_view = '/'
lm.login_message = 'realize o Login para prosseguir'
lm.login_message_category = 'alert alert-warning'
lm.init_app(app)

# -- Flask-Bcrypt
by = Bcrypt(app)

# -- Import Routes --
from routes import (
    system_user,
    system_notes,
    system_pomodoro,
    system_dashboard,
    system_stress
)

