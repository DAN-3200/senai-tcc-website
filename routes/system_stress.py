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

@app.route('/anti-stress', methods=['GET', 'POST'])
@login_required
def Anti_Stress():
    return render_template('base/stress/anti_stress.html', user=current_user)