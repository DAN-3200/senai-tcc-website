# Models do Database
from main import db
from flask_login import UserMixin

class perfil(db.Model, UserMixin):
    __tablename__ = 'perfil'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False)


    def __init__(self, nome, senha, email):
        self.nome = nome
        self.senha = senha
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.nome

class card(db.Model):
    __tablename__ = 'cards'

    id_card = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(2000))
    priority = db.Column(db.String(255))
    delete = db.Column(db.Boolean)
    fk_user = db.Column(db.Integer, db.ForeignKey('perfil.id'), nullable=False)

    def __init__(self, title, content, priority, user):
        self.title = title
        self.content = content
        self.priority = priority
        self.fk_user = user
        self.delete = False

    def __repr__(self):
        return f'<Card #{self.id_card}>'


