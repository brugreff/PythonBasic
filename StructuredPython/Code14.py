# Solução que retorne o menor elemento de uma lista

# Declarando uma função - palavra chave def
def encontrar_minimo(lista):
    minimo = lista[0] # lógica para encontrar o elemento
    for elem in lista: # programação funcional
        if(elem < minimo):
            minimo = elem
    return minimo

lista_teste = [2,10,3,1,4,5]
menor = encontrar_minimo(lista_teste)
print('O menor elemento da lista é: [{}]'.format(menor))
