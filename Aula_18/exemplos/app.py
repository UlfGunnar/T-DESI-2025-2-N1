import jinja2
import os

# Usa o diretório onde o app.py está, independente de onde o terminal foi aberto
loader = jinja2.FileSystemLoader(searchpath=os.path.dirname(os.path.abspath(__file__)))
env = jinja2.Environment(loader=loader)

# 2. Carregar o arquivo de template perfil.html
template = env.get_template("perfil.html")

# 3. Definir os dados dinâmicos que queremos passar para o template
# No mundo real, esses dados viriam de um banco de dados ou formulário.
dados_do_perfil = {
    "nome": "Ulf Gunnar Giga Chad da Silva Pettersson",
    "usuario_novo": False,
    "habilidades": [
        "Formar aurea",
        "Portugol",
        "Scratch",
        "Mente de Senior"
    ]
}

# 4. Renderizar o template com os dados
# Isso "combina" perfil.html com o dicionário dados_do_perfil
html_final = template.render(dados_do_perfil)

# 5. Salvar o resultado final em um arquivo HTML puro
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "saida_perfil.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_final)

print("Página renderizada com sucesso! Abra 'saida_perfil.html' para ver o resultado.")

