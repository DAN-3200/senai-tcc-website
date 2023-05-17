# Models do Database
from main import db

class perfil(db.Model):
    __tablename__ = 'perfil'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)

    def __init__(self, nome):
        self.nome = nome

class card(db.Model):
    __tablename__ = 'cards'

    id_card = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(255))
    priority = db.Column(db.String(255))
    delete = db.Column(db.Boolean)
    # fk_user = db.Column(db.Integer, db.ForeignKey('perfil.id'))

    def __init__(self, title, content, priority):
        self.title = title
        self.content = content
        self.priority = priority
        self.delete = False


