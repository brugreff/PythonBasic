# Função Map Lambda

# script funcao_map_lambda.py

lista = [1, 2, 3, 4, 5]

nova_lista = map(lambda item: item * 3, lista) # função lambda 
# substituição da função triplica(Code6.py) pela função lambda
# utilizada como argumento p/ função map

def main():
    print(list(nova_lista))
# func map aplica a func lambda em cada item da lista
# retorna um novo valor iterável impresso (linha 12)

if __name__ == "__main__":
    main()

# Código reduzido em relação ao Code6.py
# Preservação da utilização de func puras(lambda), alta ordem(map): preservam imutabilidade dos dados
# Garantindo que não haja efeitos colaterais e dependência de estados