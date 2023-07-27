# Se a nota for maior ou igual a 7 - Aprovado
# Se a nota for menor que 7 e maior ou igual a 5 - Recuperação
# Se a nota for menor que 5 - Reprovado

nota = 8.7

if (nota >= 7.0):
    situacao = "Aprovado"
elif (nota >= 5.0):
    situacao = "Recuperação"
else:
    situacao = "Reprovado"
print(f'O estudante está: {situacao}')
