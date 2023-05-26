# Parte lógica do site - Exibir páginas, Enviar dados ao banco...
from flask import (
    render_template,
    request,
    url_for,
    redirect
)
from flask_login import (
    login_user, # Introduz o usuário na sessão
    logout_user, # Retira o usuário da sessão
    current_user # pega o usuário da sessão
)

# coisa minha :)
from models.model import card, perfil
from main import app, db, lm
from forms.regis_form import formRegis

@lm.user_loader
def user_loader(id):
    return perfil.query.get(id)

# Entrada ------------
@app.route('/', methods=['POST','GET'])
def login():
    print(current_user)
    if request.method == "POST":
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        # remember = True if request.form.get('remember') else False

        user = perfil.query.filter_by(nome=nome).first()
        # print(f"{user}/{user.senha}")
        if user and user.senha == senha:
            login_user(user)
            return redirect(url_for('Home'))

    return render_template('login/login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

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
    print(f"{current_user.id}|{current_user}")
    cards = card.query.filter_by(fk_user=current_user.id)
    return render_template('home/criar.html', box=cards)

@app.route('/home', methods=['POST'])
def Create():
    if request.method == 'POST':
        # Request
        title = request.form['title']
        content = request.form['content']
        priority = request.form['priority']
        user = current_user.id

        # Envio ao banco
        db.session.add(card(title=title, content=content, priority=priority, user=user))
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