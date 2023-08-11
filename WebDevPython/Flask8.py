# Delimitadores especiais - são computados e subst. na renderização das págs HTML, antes de retornarem ao usuário
# Expressões: {{...}} - Escrever algo no modelo, como valor de variável 
# Declarações: {%...%} - Utilizado em laços e condicionantes(por ex.)

# Alteração da aplicação de forma que o nome passado c/ parâmetro p/ a rota '/ola/' seja exibido dentro do HTML
# Criação do arq. ola.html na pasta templates - utilizando o delimitador de expressões c/ a variável({{nome_recebido}})
# - indicando que se escreverá o conteúdo dessa variável nesse local após a renderização 

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ola.html')

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome="mundo"):
    return render_template('ola.html', nome_recebido = nome)

if __name__ == '__main__':
    app.run()