# Função Map - aplica determinada func em cada elemento de um iterável(retorna novo iterável c/ valores modificados)

# script funcao__map.py

lista = [1, 2, 3, 4, 5]

def triplica (item): # def função triplica
    return item * 3 # retorna o item passado como parâmetro 

def main():
    nova_lista = map(triplica, lista) # func triplica e variável lista: argumentos da função map
    print(list(nova_lista)) #construtor list utilizado p/ print pq a func map retorna um iterável

# map aplica internamente a func passada c/ parâm. em cada item da lista, retornando um novo iterável
# resultado da func map: é armazenado na variável nova_lista, e depois impresso (linha 12)
# func map: garante imutabilidade dos iteraveis passados como argumento

if __name__ == "__main__":
    main()