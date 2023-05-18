# validações do página de Registro
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class formRegis(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])