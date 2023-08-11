# Utilizando modelos
# Modelos: páginas HTML turbinadas(pode-se usar delimitadores especiais p/ alterar a página)

# Alterando a aplicação de forma a retornar uma página HTML ao acessar a raiz da aplicação('/')
# Criação de um arquivo chamado 'indice.html' no mesmo nível do script flask7.py

from flask import Flask, render_template

app = Flask(__name__)

# Para o modelo ser acessado na URL raiz, a função index() deve ser a resónsável por retorná-lo
# Então utiliza-se a função render_template(disponibilizada pelo Flask), recebendo o nome do arq. que se deseja retornar 
# linha 15 - "indice.html" usado como parâmetro
@app.route('/')
def index():
    return render_template('indice.html')

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome="mundo"):
    return "Olá, " + nome

if __name__ == '__main__':
    app.run()