# Métodos HTTP

from flask import Flask, request

app = Flask(__name__)
app.debug = True 
# Ativação do modo debug do servidor interno do Flask: permite melhor visualização dos avisos e erros durante o desenv.

@app.route('/')
def index():
    return "Página principal."

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome):
    return "Olá, " + nome

# Utilização do parâmetro methods do decorador @app.route()- espera uma lista de strings com o nome dos métodos aceitos
# Criação da rota p/ a função logar, passando como argumento uma lista c/ duas strings('GET' e 'POST')
# Atributo method do objeto request(retorna uma das strings:GET,POST,PUT ou DELETE): verifica o método utilizado na requisição
# Objeto request: variável global disponibilizada pelo Flask(pode ser utilizada em todas as funções)
# Obj request: permite acesso à muitas propriedades do request como cookie, parâmetros, dados de formulário etc
# Para cada requisição um novo objeto request é criado e disponibilizado

@app.route('/logar', methods=['GET', 'POST'])
def logar():
    # Atributo method do obj request: verifica o método passado na requisição e retorna conteúdos dif. dependendo do método
    if request.method == 'POST':
        return "Recebeu post! Fazer login!"
    else:
        return "Recebeu get! Exibir FORM de login."
    
if __name__ == '__main__':
    app.run()