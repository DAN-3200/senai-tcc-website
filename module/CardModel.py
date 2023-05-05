"""
Cada vez que eu inserir ou excluir um caractere do Card
o sistema deverá atualizar o conteudo do card

- vinculado ao banco

"""
from flask_sqlalchemy import SQLAlchemy # oq isso faz? é um ORM?
db = SQLAlchemy()

class card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(255), nullable=True)
    delete = db.Column(db.Boolean, nullable=True)


    def __init__(self, title, content):
        self._title = title
        self._content = content
        self._priority = 0
        self._delete = False


