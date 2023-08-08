# Boa prática de programação

# script funcao_iterable.py

lista = [1, 2, 3, 4, 5]

def triplica_itens(iterable): # func 'triplica_itens' recebe iterável como parâmetro
    lista_aux = [] # cria uma lista aux, garantindo imutabilidade
    for item in iterable: # percorre itens do iterável passado como parâmetro
        lista_aux.append(item*3) # adiciona os itens triplicados a lista aux
    return lista_aux # retorna a lista aux 

def main():
    nova_lista = triplica_itens(lista) # func é chamada c/ o argumento lista
    print(nova_lista) # resultado impresso

if __name__ == "__main__":
    main()