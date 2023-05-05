from flask import Flask, render_template, request
from module.CardModel import db, card

app = Flask(__name__)

box = [card('','')];


@app.route('/') # Raiz do endereço http
@app.route('/home')
def Home():
    return render_template('/layout/home/card.html', box=box)

@app.route('/home/update/', methods=['PUT'])
def Update():
    if request.method == 'PUT':
        dados = request.get_json()
        print(dados)

    return render_template('/layout/home/card.html', box=box)

@app.route('/home/create/')
def Create():
    box.append(card('',''))
    return render_template('/layout/home/card.html', box=box)



if __name__ == '__main__':
    app.run(debug=True)
