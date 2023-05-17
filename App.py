# Objetivo: CRUD de Cards vinculado ao BANCO - ok
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.app_context().push() # ?

# Vincula ao banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost:3306/cardbase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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


db.create_all()

@app.route('/', methods=['GET']) # Raiz do endereço http
def Home():
    cards = card.query.all()
    return render_template('home/criar.html', box=cards)

@app.route('/', methods=['POST'])
def Create():
    if request.method == 'POST':
        # Request
        title = request.form['title']
        content = request.form['content']
        priority = request.form['priority']

        # Envio ao banco
        db.session.add(card(title=title, content=content, priority=priority))
        db.session.commit()

    return redirect(url_for('Home'))

@app.route('/update/<index>', methods=['GET', 'POST'])
def Update(index):
    my_card = card.query.get(index)
    if request.method == 'POST':
        # Request
        my_card.title = request.form.get('title')
        my_card.content = request.form.get('content')
        my_card.priority = request.form.get('priority')

        db.session.commit()

        return redirect(url_for('Home'))
    else:
        return render_template('home/editar.html', card=my_card)

@app.route('/delete/<index>', methods=['GET', 'POST'])
def Delete(index):
    my_card = card.query.get(index)
    db.session.delete(my_card)
    db.session.commit()

    return redirect(url_for('Home'))

if __name__ == '__main__':
    app.run(debug=True)

    # debug=True - adapta a exibição a qualquer alteração feita no codigo em tempo real
