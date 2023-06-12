from flask import (
    render_template, # Renderizar Página
    request, # Pegar informações enviadas pelos forms
    url_for, # Caminho url do arquivo
    redirect, # Redirecionar a uma função
    jsonify, # formatar em JSON
    make_response
)
from flask_login import (
    login_user, # Introduz o usuário na sessão
    logout_user, # Retira o usuário da sessão
    current_user, # pega o usuário da sessão
    login_required, # Restringir o Usuário de acessar certas views
)
# coisa minha :)
from main import (
    app, # Aplicação
    db, # Database
    lm, # Login Manage
    by, # Flask-Bcrypt
)
from models.model import card, perfil
from forms.Forms import formRegister, formLogin

# -- CRUD de notas
@app.route('/home', methods=['GET'])
@login_required
def Home():
    print(f"{current_user.id}|{current_user}")
    cards = card.query.filter_by(fk_user=current_user.id)
    return render_template('home/criar.html', box=cards, user=current_user)

@app.route('/home', methods=['POST'])
@login_required
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
@login_required
def Update(index):
    my_card = card.query.get(index)

    if current_user.id == my_card.fk_user:
        if request.method == 'POST':
            # Request
            my_card.title = request.form.get('title')
            my_card.content = request.form.get('content')
            my_card.priority = request.form.get('priority')

            db.session.commit()

            return redirect(url_for('Home'))
        else:
            return render_template('home/editar.html', card=my_card, user=current_user)
    else:
        return redirect(url_for('Home'))

@app.route('/home/delete/<index>', methods=['GET', 'POST'])
@login_required
def Delete(index):
    my_card = card.query.get(index)
    if current_user.id == my_card.fk_user:
        db.session.delete(my_card)
        db.session.commit()

    return redirect(url_for('Home'))