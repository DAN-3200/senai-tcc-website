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
from models.model import notes

# -- CRUD de notas
@app.route('/notes', methods=['GET', 'POST'])
@login_required
def Notes():
    print(f"{current_user.id}|{current_user}")
    cards = notes.query.filter_by(fk_user=current_user.id)
    return render_template('base/notes/notes.html', box=cards, user=current_user)

@app.route('/notes/getData', methods=['POST'])
@login_required
def GetData():

    print('--- /notes/getData ---')
    Data = request.get_json()
    print(f"   {Data}")
    my_note = notes.query.get(Data.get('id'))

    return make_response(jsonify({
        'id': my_note.id,
        'title': my_note.title,
        'content': my_note.content,
        'delete': my_note.delete,
        'date': my_note.date,
    }), 200)

@app.route('/notes/create', methods=['POST'])
@login_required
def Create():
    try:
        print('--- /notes/create ---')
        # -- pega requisição JSON
        Data = request.get_json()
        print(f"   {Data}")

        # -- Parte lógica -- faça oq quiser com a informação
        title = 'Sem título'
        content = ''
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

@app.route('/notes/update', methods=['POST'])
@login_required
def Update():
    print('--- /notes/update ---')
    Data = request.get_json()
    print(f"   {Data}")
    my_note = notes.query.get(Data.get('id'))

    my_note.title = Data.get('title')
    my_note.content = Data.get('content')

    db.session.commit()

    return make_response(jsonify({
        'update':True,
    }))

@app.route('/notes/delete', methods=['POST'])
@login_required
def Delete():
    print('--- /notes/delete ---')
    Data = request.get_json()
    print(f"   {Data}")
    my_note = notes.query.get(Data.get('id'))

    db.session.delete(my_note)
    db.session.commit()

    return make_response(jsonify({
        'delete': True,
    }), 200)
