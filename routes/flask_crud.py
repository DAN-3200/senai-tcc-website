from flask import (
    render_template, # Renderizar Página
    request, # Pegar informações enviadas pelos forms
    url_for, # Caminho url do arquivo
    redirect, # Redirecionar a uma função
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
    note = notes.query.filter_by(fk_user=current_user.id)
    return render_template('home/criar.html', box=note, user=current_user)

@app.route('/home', methods=['POST'])
@login_required
def Create():
    if request.method == 'POST':
        # Request
        title = request.form['title']
        content = request.form['content']
        user = current_user.id

        # Envio ao banco
        db.session.add(notes(title=title, content=content, user=user))
        db.session.commit()

    return redirect(url_for('Home'))

@app.route('/home/update/<index>', methods=['GET', 'POST'])
@login_required
def Update(index):
    my_note = notes.query.get(index)

    if current_user.id == my_note.fk_user:
        if request.method == 'POST':
            # Request
            my_note.title = request.form.get('title')
            my_note.content = request.form.get('content')

            db.session.commit()

            return redirect(url_for('Home'))
        else:
            return render_template('home/editar.html', card=my_note, user=current_user)
    else:
        return redirect(url_for('Home'))

@app.route('/home/delete/<index>', methods=['GET', 'POST'])
@login_required
def Delete(index):
    my_note = notes.query.get(index)
    if current_user.id == my_note.fk_user:
        db.session.delete(my_note)
        db.session.commit()

    return redirect(url_for('Home'))