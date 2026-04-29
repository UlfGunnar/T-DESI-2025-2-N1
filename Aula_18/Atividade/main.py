from flask import Flask, render_template
from fonte_dados import musicJ
import jinja2
import os

loader = jinja2.FileSystemLoader(searchpath=os.path.dirname(os.path.abspath(__file__)))
env = jinja2.Environment(loader=loader)

template = env.get_template("playlist.html")

html_final = template.render(musicJ=musicJ)

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"templates", "saida_playlist.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_final)

print("Página renderizada com sucesso! Abra 'saida_playlista.html' para ver o resultado.")

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('saida_playlist.html')

if __name__ == '__main__':
    app.run(debug=True)