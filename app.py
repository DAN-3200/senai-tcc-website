from main import app, db

# db.drop_all()
# db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
    # 'debug=True' - adapta a exibição a qualquer alteração feita no codigo em tempo real
