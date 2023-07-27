# Somar todos os números pares de uma lista

# Estratégia 01
lista = [10, 2, 5, 7, 6, 3]
n = len(lista) # calcula o comprimento da lista
soma = 0

for i in range(n): # varredura da lista em um intervalo, pega as posições
    if(lista[i]%2==0): #se o resto da div de i por 2 for zero
        soma = soma + lista[i]

print(f'O somatório dos elementos pares da lista é: {soma}')

# Estratégia 02
# usa melhor a programação funcional
lista = [10, 2, 5, 7, 6, 3]

soma   = 0
for num in lista: # pega os elementos da lista 
    if(num%2==0):  
        soma = soma + num

print(f'O somatório dos elementos pares da lista é: {soma}')