# Importação da classe flask(classe principal do framework)
from flask import Flask

# Criação de uma instância da classe flask
# Passando '__name__ como argumento
# Assim o Flask consegue localizar, na aplicação, arq. estáticos, como css e javascript, e arquivos de modelos(templates)
app = Flask(__name__)

# Decorador @app.route('/') - Criação de uma rota p/ a URL raiz da aplicação('/')
# - espera como parâmetro a rota, ou URL, que será utilizada no navegador(por ex.)
# A requisição feita p/ uma rota é encaminhada p/ a função abaixo do decorador: função ola_mundo
# - retorno dessa função é a resposta do servidor ao usuário
@app.route('/') 
def ola_mundo():
    return "Olá, mundo!"

# Ao digitar no navegador a URL http://127.0.0.1:5000, a frase "Olá, mundo!" será exibida

if __name__ == '__main__':
    app.run()