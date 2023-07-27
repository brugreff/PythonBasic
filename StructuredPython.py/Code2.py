# Solução que verifiique se um nº é par ou ímpar.

numero = eval(input('Digite um número inteiro:'))

if(numero % 2 == 0):
    situacao = "O número é par"
else:
    situacao = "O número é ímpar"
print(situacao)