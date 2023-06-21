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
from models.model import rascunho, todo

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def Dashboard():
    papel = rascunho.query.filter_by(fk_user=current_user.id).first()
    lista = todo.query.filter_by(fk_user=current_user.id)
    return render_template("base/dashboard/dashboard.html", user=current_user, papel=papel, lista=lista)

@app.route('/sketch', methods=['GET', 'POST'])
@login_required
def sketch():
    Data = request.get_json()
    print(Data.get('text'))

    ras = rascunho.query.filter_by(fk_user=current_user.id).first()
    ras.content = Data.get('text')
    db.session.commit()

    return make_response(jsonify({
        'status': True,
    }))