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
from models.model import sketch, notes

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def Dashboard():
    rascunho = notes.query.filter_by(fk_user=current_user.id) or False
    return render_template("base/dashboard/dashboard.html", user=current_user, sketch=rascunho)

@app.route('/sketch', methods=['GET', 'POST'])
def sketch():
    Data = request.get_json()
    print(Data.get('text'))

    rascunho = sketch(Data.get('text'), current_user.id)

    db.session.add(rascunho)
    db.session.commit()

    return make_response(jsonify({
        'id' : rascunho.id,
        'status': True,
    }))