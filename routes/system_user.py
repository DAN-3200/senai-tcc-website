from flask import (
    render_template, # Renderizar Página
    request, # Pegar informações enviadas pelos forms
    url_for, # Caminho url do arquivo
    redirect, # Redirecionar a uma função
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
    by, # Flask-Bcrypt
)
from models.model import perfil, rascunho
from forms.Forms import formRegister, formLogin

def Begin_Data(id):
    db.session.add(rascunho(id))
    db.session.commit()

@app.route('/', methods=['POST','GET'])
def Start():
    return render_template('inicio/start.html')

# -- Login/Register
@app.route('/login', methods=['POST','GET'])
def login():
    # Agora Loga tanto com Username quanto com Email
    if request.method == "POST":
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        remember = True if request.form.get('remember') else False

        user = perfil.query.filter_by(nome=nome).first() or perfil.query.filter_by(email=nome).first()
        if user and by.check_password_hash(user.senha, senha):
            login_user(user, remember=remember)
            return redirect(url_for('Dashboard'))

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
            newUser = perfil(
                nome=request.form.get('nome'),
                senha=by.generate_password_hash(request.form.get('senha')), # senha scriptada
                email=request.form.get('email')
            )
            db.session.add(newUser)
            db.session.commit()

            Begin_Data(newUser.id)
            return redirect(url_for('login'))

    return render_template('register/register.html', form=formRegister())

