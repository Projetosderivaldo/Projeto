from flask import Flask, request, render_template_string, redirect, render_template
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

from flask_login import logout_user



app = Flask(__name__)
app.secret_key = 'super secret string'  # Altere isso!

# Configuração do Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Dicionário para armazenar usuários, nomes e senhas
usuarios = {
    'derivaldo.henrique': {'nome': 'Derivaldo Henrique', 'senha': '000'},
    'gustavo.martins': {'nome': 'Gustavo Martins', 'senha': '111'},
    'osias.rocha': {'nome': 'Osias Rocha', 'senha': '222'}
}

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(username):
    if username not in usuarios:
        return

    user = User()
    user.id = username
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Verificar as credenciais do usuário
        if username in usuarios and usuarios[username]['senha'] == password:
            user = User()
            user.id = username
            login_user(user)
            # Redirecionar para a rota do menu após a autenticação bem-sucedida
            return redirect('/menu')
        else:
            error = 'Senha ou usuário errados'

    return render_template_string('''
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Calibri');
            body {background-color: white; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; font-family: 'Calibri';}
            h1   {color: white; font-size: 1.2em;}
            div  {border: 2px solid #333; padding: 20px; width: 300px; border-radius: 15px; background-color: #333; box-shadow: 0px 0px 10px 5px #333;}
            label {display: block; margin-top: 20px;}
            input[type="text"], input[type="password"] {width: 100%; padding: 10px; margin-bottom: 15px; border-radius: 5px;}
            input[type="submit"] {width: 100%; padding: 10px; background-color: white; color: black; border: none; border-radius: 5px;}
            .logo {position: absolute; top: 0; left: 0; width: 150px; border-radius: 50%;}
            .error {color:red;}
        </style>
        <body>
            <img class="logo" src="/static/logo.png" alt="Logo da empresa">
            <div>
                <h1>Login</h1>
                <form method="post" autocomplete="off">
                    <label for="username">Nome de usuário:</label>
                    <input type="text" id="username" name="username" autocomplete="username">
                    <label for="password">Senha:</label>
                    <input type="password" id="password" name="password" autocomplete="new-password">
                    <input type="submit" value="Login">
                </form>
                {% if error %}
                <p class="error">{{ error }}</p>
                {% endif %}
            </div>
        </body>
    ''', error=error)

@app.route('/menu')
@login_required
def menu():
    return render_template('menu.html')

from flask_login import logout_user

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

if __name__ == '__main__':
    app.run(port=3000)



















