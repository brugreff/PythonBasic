# Rotas e Parâmetros - Aprimorando rotas
# Acertando a função para criar também uma rota p/ a URL raiz da aplicação

from flask import Flask

app = Flask(__name__)

# Chamando a função dessa rota de index e criando a rota
@app.route('/')
def index():
    return "Página principal."

@app.route('/ola')
def ola_mundo():
    return "Olá, mundo!"

if __name__ == '__main__':
    app.run()