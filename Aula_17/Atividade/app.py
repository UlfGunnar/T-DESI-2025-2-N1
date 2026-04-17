from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pagina_sobremim():
    return '<h1>Sobre mim</h1> <p>Nome: Ulf Gunnar</p> <p>Turma: T-DESI-2025-2-N1</p> <p>Tema: Veterinário</p>'

@app.route('/Login')
def pagina_login():
    return "<h1>Tela de login</h1>"

@app.route('/Cadastro')
def pagina_cadastro():
    return '<h1>Tela de cadastro</h1>'

@app.route('/Sobre')
def pagina_sobre():
    return '<h1>Sobre mim</h1> <p>Nome: Ulf Gunnar</p> <p>Turma: T-DESI-2025-2-N1</p> <p>Tema: Veterinário</p>'

@app.route('/LoginSA')
def pagina_loginSA():
    return render_template('Login.html')

@app.route('/Teste')
def pagina_teste():
    return render_template('teste.html')

@app.route('/ping')
def pagina_ping():
    return '<h1>Ping</h1><br><h6>Pong!</h6>'

@app.route('/erro')
def pagina_erro():
    return f'<h1>{10 /0}</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=8080)