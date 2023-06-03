from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class formRegister(FlaskForm):
    nome = StringField('nome', validators=[DataRequired(), Length(4, 20)])
    email = EmailField('email', validators=[DataRequired(), Length(10, 60)])
    senha = PasswordField('senha', validators=[DataRequired(), Length(4, 15)])
    c_senha = PasswordField('c_senha', validators=[DataRequired(), Length(4, 15), EqualTo('senha')])

    submit = SubmitField('continue')


class formLogin(FlaskForm):
    nome = StringField('nome', validators=[DataRequired(), Length(4, 20)])
    senha = PasswordField('senha', validators=[DataRequired(), Length(4, 10)])
    remember = BooleanField("remember")