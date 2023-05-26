# validações do página de Registro
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

class formRegis(FlaskForm):
    nome = StringField('nome', validators=[DataRequired(), Length(4, 20)])
    senha = PasswordField('senha', validators=[DataRequired(), Length(4, 10)])