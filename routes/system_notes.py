from flask import (
    render_template, # Renderizar Página
    request, # Pegar informações enviadas pelos forms
    url_for, # Caminho url do arquivo
    redirect, # Redirecionar a uma função
    jsonify, # formatar em JSON
    make_response
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
from models.model import notes

# -- CRUD de notas
@app.route('/home', methods=['GET'])
@login_required
def Home():
    print(f"{current_user.id}|{current_user}")
    cards = notes.query.filter_by(fk_user=current_user.id)
    return render_template('home/note.html', box=cards, user=current_user)

@app.route('/notes/create', methods=['POST'])
@login_required
def create():
    try:
        print('--- /notes/create ---')
        # -- pega requisição JSON
        Data = request.get_json()
        print(f"   {Data}")

        # -- Parte lógica -- faça oq quiser com a informação
        title = 'Sem título'
        content = 'Conteudo...'
        user = current_user.id

        note = notes(title=title, content=content, user=user)
        db.session.add(note)
        db.session.commit()

        # -- formate a nova informação em JSON e retorne
        return make_response(jsonify({
            'id': note.id,
            'create': True,
        }), 200)
    except:
        return make_response(jsonify({'create': False}), 200)

@app.route('/home/getData/', methods=['GET', 'POST'])
@login_required
def getData(index):

    print('--- /home/update/ ---')
    Data = request.get_json()
    my_note = notes.query.get(Data.get('id'))

    return make_response(jsonify({
        'id': my_note.id,
        'title': my_note.title,
        'content': my_note.content,
        'delete': my_note.delete,
        'date': my_note.date,
    }), 200)

@app.route('/home/delete/<index>', methods=['GET', 'POST'])
@login_required
def Delete(index):
    my_card = notes.query.get(index)
    if current_user.id == my_card.fk_user:
        db.session.delete(my_card)
        db.session.commit()

    return redirect(url_for('Home'))