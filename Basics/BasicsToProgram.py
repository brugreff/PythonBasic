nome = input('Entre com o seu nome: ')
print(nome)

numero = eval(input('Entre com um inteiro: '))
numero = numero + 2
print(numero)
print(type(numero))

# função eval():recebe uma string, mas trata como valor numérico
s = '1 + 2'
print(type(s))
print(eval(s))
