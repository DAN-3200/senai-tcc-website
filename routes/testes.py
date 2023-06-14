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

# -- implementações
@app.route('/profile', methods=['GET'])
def profile():
    file = url_for('static', filename='img/Setup-bro.png')
    return render_template('test/profile.html', user=current_user, file=file)

@app.route('/config', methods=['GET', 'POST'])
def config():
    user = perfil.query.get(current_user.id)
    if request.method == "POST":
        user.senha = by.generate_password_hash(request.form.get('senha'))
        db.session.commit()
        return redirect(url_for('Home'))

    return render_template('test/config.html', form=formRegister(), user=current_user.nome)

# -- Testando AJAX
@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('new/dashboard.html')

@app.route('/ajax', methods=['GET', 'POST'])
def ajax():
    try:
        print('--- JS/URL/ON ---')

        # -- pega requisição JSON
        Data = request.get_json()
        print(f"  {Data}")
        # -- Parte lógica -- faça oq quiser com a informação
        ent = perfil.query.get(Data.get('Titulo'))

        print(f"  {ent.email}")
        # -- formate a nova informação em JSON e retorne
        newData = make_response(jsonify({ 'Email' : ent.email }), 200)

        return newData
    except:
        return make_response(jsonify({ 'Email' : 'None'}), 200)