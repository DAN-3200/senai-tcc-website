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

@app.route('/toDo', methods=['GET', 'POST'])
def toDo():
    cards = card.query.filter_by(fk_user=current_user.id)
    return render_template('test/H.html', box=cards)

@app.route('/ajax/create', methods=['GET', 'POST'])
def create_AJAX():
    try:
        print('--- /ajax/create/on ---')

        # -- pega requisição JSON
        Data = request.get_json()
        print(f"  {Data}")

        # -- Parte lógica -- faça oq quiser com a informação

        title = Data.get('word')
        content = ''
        priority = ''
        user = current_user.id

        # Envio ao banco
        db.session.add(card(title=title, content=content, priority=priority, user=user))
        db.session.commit()

        # -- formate a nova informação em JSON e retorne
        newData = make_response(jsonify({'status': True}), 200)

        return newData
    except:
        return make_response(jsonify({ 'status' : False}), 200)

@app.route('/ajax/update', methods=['GET', 'POST'])
def update_AJAX():
    pass

@app.route('/ajax/delete', methods=['GET', 'POST'])
def delete_AJAX():
   pass