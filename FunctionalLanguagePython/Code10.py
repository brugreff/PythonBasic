# Função filter lambda 

# script funcao_filter_lambda.py

lista = [1, 2, 3, 4, 5]

nova_lista = filter(lambda item: item % 2 != 0, lista)
# substituição da func ímpar(Code9.py) pela func lambda
# func lambda utilizada como argumento p/ a func filter 
# func filter aplica a func lambda para cada item da lista

def main():
    print(list(nova_lista)) # impressão da nova lista

if __name__ == "__main__":
    main()