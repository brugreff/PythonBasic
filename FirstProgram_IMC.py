# Calcular e informar o IMC do usuário

peso = eval(input('Entre com o seu peso: '))
altura = eval(input('Entre com a sua altura: '))

IMC = peso / (altura**2)
print('IMC =', IMC)
