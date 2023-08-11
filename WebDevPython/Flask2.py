# Rotas e Parâmetros - Aprimorando rotas

# Alteração Flask1.py: a rota p/ função ola_mundo será http://127.0.0.1:5000/ola

from flask import Flask

app = Flask(__name__)

@app.route('/ola')
def ola_mundo():
    return "Olá, mundo!"

if __name__ == '__main__':
    app.run()

# Ao acessar a URL http://127.0.0.1:5000/ola - "Olá, mundo!" será obtido como resposta.
# Ao acessar a URL http://127.0.0.1:5000 - Um erro(404) de página não encontrada(Not Found) é apresentado
# - a rota p/ a URL raiz da aplicação não existe mais
