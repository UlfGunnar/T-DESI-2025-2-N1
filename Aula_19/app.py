from flask import Flask, request, redirect, url_for, render_template, flash
import os

class Livro:
    def __init__(self, titulo: str, autor: str, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

class LivroDAO:
    def __init__(self):
        self.banco_de_dados = []

    def Salvar(self, livro_novo):
        self.banco_de_dados.append({
            "titulo": livro_novo.titulo,
            "autor": livro_novo.autor,
            "paginas": livro_novo.paginas
        })

    def Listar(self):
        return self.banco_de_dados

def menor_zero(num_paginas):
    if num_paginas <= 0:
        raise ValueError('O Livro tem que ter ao menos 1 página')
    return num_paginas

dao = LivroDAO()
app = Flask(__name__)
app.secret_key = "chave_secreta"

@app.route('/novo_livro', methods=['GET', 'POST'])
def novo_livro():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        paginas = request.form.get('paginas')

        try:
            paginas = int(paginas)
            menor_zero(paginas)
        except ValueError as e:
            flash(f"Erro: Falha no cadastro por {e}")
            return redirect(url_for('novo_livro'))

        livro_novo = Livro(titulo, autor, paginas)
        dao.Salvar(livro_novo)
        return redirect(url_for('novo_livro'))

    return render_template('formulario.html')

@app.route('/lista')
def lista_livros():
    livros = dao.Listar()
    return render_template('lista.html', livros=livros)

if __name__ == "__main__":
    app.run()