# Models do Database
import datetime
from main import db, lm
from flask_login import UserMixin

@lm.user_loader
def user_loader(id):
    return perfil.query.get(id)

class perfil(db.Model, UserMixin):
    __tablename__ = 'perfil'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, senha, email):
        self.nome = nome
        self.senha = senha
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.nome

class notes(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(4000))
    delete = db.Column(db.Boolean)
    date = db.Column(db.Date, default=datetime.datetime.now().date)

    fk_user = db.Column(db.Integer, db.ForeignKey('perfil.id'), nullable=False)

    def __init__(self, title, content, user):
        self.title = title
        self.content = content
        self.fk_user = user

    def __repr__(self):
        return f'<Card #{self.id}>'

class todo(db.Model):

    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    content = db.Column(db.String(255), nullable=False)
    check = db.Column(db.Boolean)

    fk_user = db.Column(db.Integer, db.ForeignKey('perfil.id'), nullable=False)
    def __init__(self, content, user):
        self.content = content
        self.fk_user = user

class rascunho(db.Model):
    __tablename__ = "rascunho"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fk_user = db.Column(db.Integer, db.ForeignKey('perfil.id'), nullable=False)
    content = db.Column(db.String(500))
    def __init__(self, fk_user):
        self.fk_user = fk_user

class pomodoro(db.Model):
    __tablename__ = "pomodoro"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fk_user = db.Column(db.Integer, db.ForeignKey('perfil.id'), nullable=False)
    normal = db.Column(db.Float, nullable=False, default=25)
    short = db.Column(db.Float, nullable=False, default=5)
    long = db.Column(db.Float, nullable=False, default=15)
    def __int__(self, normal, short, long):
        self.normal = normal
        self.short = short
        self.long = long