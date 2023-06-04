from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo
from models.model import perfil

class formRegister(FlaskForm):
    nome = StringField('nome', validators=[DataRequired(), Length(4, 40)])
    email = EmailField('email', validators=[DataRequired(), Length(10, 100)])
    senha = PasswordField('senha', validators=[DataRequired(), Length(4, 20)])
    c_senha = PasswordField('c_senha', validators=[DataRequired(), Length(4, 20), EqualTo('senha')])

    submit = SubmitField('continue')

    def validate_nome(self, nome):
        Username = perfil.query.filter_by(nome=nome).first()
        if Username:
            raise ValidationError('Esse username já existe')

    def validate_email(self, email):
        Email = perfil.query.filter_by(email=email).first()
        if Email:
            raise ValidationError('Esse Email já existe')

class formLogin(FlaskForm):
    nome = StringField('nome', validators=[DataRequired(), Length(4, 100)])
    senha = PasswordField('senha', validators=[DataRequired(), Length(4, 20)])
    remember = BooleanField("remember")

    submit = SubmitField('entrar')
