# a. Exibir a mensagem:"Olá, programadores!" no endereço raiz de uma pág web e apareça o link "/user/Usuário"
# b. Exibir a mensagem:"Olá, Usuário!" no endereço "user/" e exibir a mensagem "Altere o endereço do browser e recarregue a página"
# c. Exibir a mensagem: "Olá, nome_usuário!" no endereço "/user/nome_do_usuario" de uma página web 

# Outra forma de fazer, sem criar novo arquivo em formato html

from flask import Flask
app = Flask(__name__)

@app.route('/')
def cumprimento():
    boas_vindas = '<h1>Olá, programadores!</h1>'
    link = '<p><a href="user/Usuário">Clique Aqui!</a></p>'
    return boas_vindas + link 

@app.route('/user/')
@app.route('/user/<nome>')
def user (nome="Usuário"):
    personalizar = f'<h1>Olá, {nome}!</h1>'
    instrucao = '<p>Altere o nome no <em> endereço do browser</em> e recarregue a página.</p>'
    return personalizar + instrucao

if __name__ == '__main__':
    app.run(debug=True)