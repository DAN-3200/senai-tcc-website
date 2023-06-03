from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length

class formRegister(FlaskForm):
    nome = StringField('nome', validators=[DataRequired(), Length(4, 20)])
    email = EmailField('email', validators=[DataRequired(), Length(10, 60)])
    senha = PasswordField('senha', validators=[DataRequired(), Length(4, 15)])
    c_senha = PasswordField('c_senha', validators=[DataRequired(), Length(4, 15)])

class formLogin(FlaskForm):
    nome = StringField('nome', validators=[DataRequired(), Length(4, 20)])
    senha = PasswordField('senha', validators=[DataRequired(), Length(4, 10)])