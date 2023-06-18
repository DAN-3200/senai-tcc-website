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

@app.route('/pomodoro', methods=['GET', 'POST'])
@login_required
def Pomodoro():
    return render_template('base/pomodoro/pomodoro.html', user=current_user)