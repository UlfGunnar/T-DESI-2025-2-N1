from flask import Flask, request, redirect, url_for, render_template, flash
import jinja2
import os

class livro:
    def __init__(self, titulo: str, autor: str, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

class livroDAO:
    def __init__(self):
        self.banco_de_dados = []

    def Salvar(self, livro_novo):
        dados_do_livro = {
            "titulo": livro_novo.titulo,
            "autor": livro_novo.autor,
            "paginas": livro_novo.paginas
        }

        self.banco_de_dados.append(dados_do_livro)

    def Listar(self):
        return self.banco_de_dados

def menor_zero(num_paginas):
    if num_paginas <= 0:
        raise ValueError('O Livro tem que ter ao menos 1 página')
    return num_paginas








dao = livroDAO()
app = Flask(__name__)
app.secret_key = "chave_secreta"

@app.route('/novo_livro')
def novo_livro():
    return render_template('formulario.html')

@app.route('/novo_livro', methods=['POST'])
def processar_novo_livro():
    titulo = request.form.get('titulo')
    autor = request.form.get('autor')
    paginas = request.form.get('paginas')

    try:
        paginas = int(paginas)
        menor_zero(paginas)
    except ValueError as e:
        flash(f"Erro: Falha no cadastro por {e}")
        return redirect(url_for('novo_livro'))
    
    novo_livro = livro(titulo, autor, paginas)
    dao.Salvar(novo_livro)

    return redirect(url_for('novo_livro'))

@app.route('/lista')
def lista_livros():
    loader = jinja2.FileSystemLoader(
    searchpath=os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")  # ← adiciona "templates"
    )
    env = jinja2.Environment(loader=loader)

    template = env.get_template("lista.html")  
    livros = dao.Listar()  
    html_final = template.render(livros=livros)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"templates", "saida_lista.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_final)

    print("Página renderizada com sucesso! Abra 'saida_playlista.html' para ver o resultado.")
    
    return html_final

if __name__ == "__main__":
    app.run()


    
