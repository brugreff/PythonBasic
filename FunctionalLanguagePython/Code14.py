# Programação Funcional

# Implementar solução p/ somar todos os elementos da lista.

# utilizar função reduce
from functools import reduce

f_soma = lambda x,y: x + y

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # lista em questão

# aplicando a soma para todos os elementos da lista
resultado = reduce(f_soma, numeros)

print(resultado)
