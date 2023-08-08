# Função filter: filtra elem. de um iterável 
# É func pura e de alta ordem: depende apenas dos parâmetros e recebe uma func como parâmetro
# Utiliza uma função(capaz de retornar True ou False) para cada elemento do iterável
# Sempre retorna um iterável(mesmo vazio)

# Todo elemento TRUE: é incluído em um novo iterável retornado pela func filter
# Sintaxe: filter(função, iterável)

# script funcao_filtro_iterable.py

lista = [1, 2, 3, 4, 5]

def impares(iterable): # def func ímpares, recebe um iterável como parâmetro
    lista_aux = [] # cria lista aux(garantir imutabilidade)
    for item in iterable: # percorre itens do iterável passados c/ parâmetro
        if item % 2 != 0: # faz o reconhecimento dos números ímpares
            lista_aux.append(item) # os add à lista aux
    return lista_aux 

def main():
    nova_lista = impares(lista) # func ímpares é chamada com o argumento lista
    print(nova_lista) # resultado impresso

if __name__ == "__main__":
    main()