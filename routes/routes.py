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

@lm.user_loader # ainda não sei pra que serve isso, mas é necessário pra o Login-Manager
def user_loader(id):
    return perfil.query.get(id)

# -- Login/Register
@app.route('/', methods=['POST','GET']) # Raiz do endereço http
def login():
    # Agora Loga tanto com Username quanto com Email
    if request.method == "POST":
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        remember = True if request.form.get('remember') else False

        user = perfil.query.filter_by(nome=nome).first() or perfil.query.filter_by(email=nome).first()
        if user and by.check_password_hash(user.senha, senha):
            login_user(user, remember=remember)
            return redirect(url_for('Home'))

    return render_template('login/login.html', form=formLogin())

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        if request.form.get('senha') == request.form.get('c_senha'):
            db.session.add(perfil(
                nome=request.form.get('nome'),
                senha=by.generate_password_hash(request.form.get('senha')), # senha scriptada
                email=request.form.get('email')
            ))
            db.session.commit()
            return redirect(url_for('login'))

    return render_template('register/register.html', form=formRegister())

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

# -- implementações
@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('test/engine.html')

@app.route('/config', methods=['GET', 'POST'])
def config():
    user = perfil.query.get(current_user.id)
    if request.method == "POST":
        user.senha = by.generate_password_hash(request.form.get('senha'))

        db.session.commit()
        return redirect(url_for('Home'))

    return render_template('test/config.html', form=formRegister(), user=current_user.nome)

# -- Testando AJAX
@app.route('/ajax', methods=['GET', 'POST'])
def ajax():
    try:
        print('--- JS/URL/ON ---')

        # -- pega requisição JSON
        Data = request.get_json()
        print(Data)
        # -- Parte lógica -- faça oq quiser com a informação
        ent = perfil.query.get(Data.get('Titulo'))

        print(ent.email)
        # -- formate a nova informação em JSON e retorne
        newData = make_response(jsonify({ 'Email' : ent.email }), 200)

        return newData
    except:
        return make_response(jsonify({ 'Email' : 'None'}), 200)
