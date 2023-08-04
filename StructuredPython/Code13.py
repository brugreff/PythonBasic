# Instrução aux - pass: atua sobre o if
# usa-se quando se quer criar uma função q faça algo específico, 
# mas não se sabe ainda exatamente o que fazer
# evitar erro de sintaxe e conseguir rodar o código
# deve ser substituído por código real quando souber o que implementar

# imprimindo somente os num ímpares entre 1 e 10

for num in range(1, 11): # sempre terminar com i+1
    if num % 2 == 0:
        pass
    else:
        print(num)
print('Laço encerrado.')
