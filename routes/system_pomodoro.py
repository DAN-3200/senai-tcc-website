from flask import (
    render_template, # Renderizar Página
    request, # Pegar informações enviadas pelos forms
    jsonify, # formatar em JSON
    make_response, # formartar uma respostar HTTP
)
from flask_login import (
    current_user, # pega o usuário da sessão
    login_required, # Restringir o Usuário de acessar certas views
)
# coisa minha :)
from main import (
    app, # Aplicação
    db, # Database
)
from models.model import todo

@app.route('/pomodoro', methods=['GET', 'POST'])
@login_required
def Pomodoro():
    card = todo.query.filter_by(fk_user=current_user.id)
    return render_template('base/pomodoro/pomodoro.html', user=current_user, box=card)

@app.route('/ajax/create', methods=['GET', 'POST'])
def create_AJAX():
    try:
        print('--- /ajax/create ---')

        # -- pega requisição JSON
        Data = request.get_json()
        print(f"   {Data}")

        # -- Parte lógica -- faça oq quiser com a informação
        content = Data.get('content')
        user = current_user.id

        card = todo(content=content, user=user)

        # Envio ao banco
        db.session.add(card)
        db.session.commit()

        # -- formate a nova informação em JSON e retorne
        return make_response(jsonify({
            'id': card.id,
            'content': card.content,
            'create': True,
        }), 200)

    except:
        return make_response(jsonify({'create': False}), 200)

@app.route('/ajax/update', methods=['GET', 'POST'])
def update_AJAX():
    try:
        print('--- /ajax/update ---')

        # -- pega requisição JSON
        Data = request.get_json()
        print(f"  {Data}")

        # -- lógica --
        my_card = todo.query.get(Data.get('id'))
        my_card.content = Data.get('content')
        db.session.commit()

        return make_response(jsonify({'update': True}), 200)
    except:
        return make_response(jsonify({'update': False}), 200)

@app.route('/ajax/delete', methods=['GET', 'POST'])
def delete_AJAX():
    try:
        print('--- /ajax/delete ---')

        # -- pega requisição JSON
        Data = request.get_json()
        print(f"  {Data}")

        # -- lógica --
        my_card = todo.query.get(Data.get('id'))
        db.session.delete(my_card)
        db.session.commit()

        return make_response(jsonify({'delete': True}), 200)
    except:
        return make_response(jsonify({'delete': False}), 200)