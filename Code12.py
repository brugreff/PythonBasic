# Laço while infinito
# Instrução aux-continue:interrompe apenas a iteração corrente, passando o loop para a próx iteração

for num in range(1, 11):
    if num %2 != 0: # condiciona que deve pular os ímpares
        continue
    else:
        print(num)
print('Laço encerrado.')