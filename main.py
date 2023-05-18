from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Vincula ao banco --------------
usuario_db = "root" ; senha_db = "1234" ; banco_db = "cardbase"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{usuario_db}:{senha_db}@localhost:3306/{banco_db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# formulário --------------
app.config['SECRET_KEY'] = 'nome-seguro-baby'

app.app_context().push()
db = SQLAlchemy(app)



