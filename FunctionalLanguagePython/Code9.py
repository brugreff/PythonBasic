# Função filter 

# script funcao_filter.py

lista = [1, 2, 3, 4, 5]

def impar(item): # def func ímpar
    return item % 2 != 0
    # retorna True se o item parâmetro é ímpar ou False caso contrário

def main():
    nova_lista = filter(impar, lista) # func impar e variável lista: parâmetros p/ função filter
    print(list(nova_lista))
# Filter irá aplicar internamente a func passada como parâmetro em cada elem da lista
# Retorna um novo iterável
# Resultado da func filter é armazenado na var nova_lista e impresso (linha 13)
# Uso do construtor list p/ imprimir o resultado

if __name__ == "__main__":
    main()