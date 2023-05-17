# Objetivo: CRUD de Cards vinculado ao BANCO - ok
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Vincula ao banco
user_db = "root" ; senha_db = "root" ; banco_db = "bank"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{user_db}:{senha_db}@localhost:3306/{banco_db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()
db = SQLAlchemy(app)



