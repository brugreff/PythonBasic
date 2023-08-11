# Recebendo parâmetros

from flask import Flask

app = Flask(__name__)

# Decorador de rota(route) permite que sejam passados parâmetros p/ as funções
# - colocar o nome do parâmetro da função entre <> na URL da rota

@app.route('/')
def index():
    return "Página principal."

# Variável nome: mesmo nome do parâmetro da função ola_mundo
# - indica que qlqr valor adicionado a URL após o '/ola/' será passado como arg. p/ variável nome da função ola_mundo
@app.route('/ola/<nome>') 
def ola_mundo(nome):
    return "Olá, " + nome

if __name__ == "__main__":
    app.run()

# Acessando a URL http://127.0.0.1:5000/ola/Amigo recebemos: "Olá, Amigo"
# Acessando a URL http://127.0.0.1:5000/ola/Fulano recebemos: "Olá, Fulano"
# Porém acessando a URL http://127.0.0.1:5000/ola/ recebemos um erro, pois a rota p/ essa URL foi removida 