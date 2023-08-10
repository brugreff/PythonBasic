# Programação funcional

# Implementar solução p/ imprimir somente os numeros pares da lista.

lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] 

fTesteParidade = lambda x: x % 2 == 0 # utilização função lambda 
# Irá receber um parâmetro da lista e testar sua paridade 
# Retornará um valor booleano (V ou F)
# Se resto = 0, V, nº é par / Se resto != 0, F, nº não é par

print(f'teste de fTesteParidade(5) = {fTesteParidade(5)}')
# print para testar se fTesteParidade está ok

pares = list(filter(fTesteParidade, lista))
# filter() - irá aplica um filtro na lista 
# transformando em uma nova lista

print(f"lista de números pares = {pares}")
# impressão dos resultados apenas com os elementos pares 