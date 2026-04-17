from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('index copy.html')

@app.route('/contato')
def exibir_contato():
    return "<p>email: ulfgunnar6@gmail.com</p> <p>Celular: 4002-8922</p>"

if __name__ == '__main__':
    app.run(debug=True)