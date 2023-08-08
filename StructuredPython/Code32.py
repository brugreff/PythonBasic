# Captura de exceções de determinado tipo
# Py permite que o bloco relativo ao except seja executado somente caso a exceção levantada seja de determinado tipo
# Então o except deve trazer o tipo de exceção desejada

# Exemplo com captura apenas das exceções do tipo NameError

try:
    num = eval(input("Entre com um número inteiro: \n"))
    print(num)
except NameError: # especifica a exceção
    print("Entre com o valor numérico e não letras")