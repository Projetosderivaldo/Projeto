from flask import Flask, render_template
# Importar o arquivo Login-flask.py
import telalogin

app = Flask(__name__)

# Rota para a segunda tela após o login
@app.route('/menu')
def menu():
    # Renderizar o template HTML com os menus
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(port=3000)
