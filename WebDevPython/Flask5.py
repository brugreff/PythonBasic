# Recebendo parâmetros
# Corrigindo o erro da URL http://127.0.0.1:5000/ola (Flask4.py)

# Adicionar uma segunda rota para a mesma função
# - add outro decorador @app.route p/ uma mesma função ola_mundo

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Página principal."

@app.route('/ola/') # 1ª rota p/ função ola_mundo
@app.route('/ola/<nome>') # 2ª rota p/ função ola_mundo
def ola_mundo(nome='mundo'): # def. o valor padrão "mundo" como parâmetro
    return "Olá, " + nome
# Em qualquer uma das URLs o usuário será redirecionado p/ a função ola_mundo

if __name__ == '__main__':
    app.run()

# Acessando a URL http://127.0.0.1:5000/ola/Amigo recebemos: "Olá, Amigo"
# Acessando a URL http://127.0.0.1:5000/ola/Fulano recebemos: "Olá, Fulano"
# Porém acessando a URL http://127.0.0.1:5000/ola/ recebemos: "Olá, mundo" 