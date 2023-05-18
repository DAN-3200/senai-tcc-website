# Objetivo: CRUD de Cards vinculado ao BANCO
from flask import render_template, request, url_for, redirect

# coisa minha :)
from models.model import card, perfil
from main import db, app
from forms.regis_form import formRegis

# Entrada ------------
@app.route('/', methods=['POST','GET'])
def login():
    return render_template('login/login.html')
@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        print(request.form)

        db.session.add(perfil(request.form.get('nome'), request.form.get('senha')))
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register/cadastro.html', form=formRegis())


# DashBoard ----------
@app.route('/home', methods=['GET']) # Raiz do endereço http
def Home():
    cards = card.query.all()
    return render_template('home/criar.html', box=cards)

@app.route('/home', methods=['POST'])
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

@app.route('/home/update/<index>', methods=['GET', 'POST'])
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

@app.route('/home/delete/<index>', methods=['GET', 'POST'])
def Delete(index):
    my_card = card.query.get(index)
    db.session.delete(my_card)
    db.session.commit()

    return redirect(url_for('Home'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

    # debug=True - adapta a exibição a qualquer alteração feita no codigo em tempo real