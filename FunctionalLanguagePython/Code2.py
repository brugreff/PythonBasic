# Função pura

# Exemplo - script funcao2.py

# variável valor e função número como parâmetros p/ função multiplica 

valor = 20

def multiplica(valor, fator): # função multiplica - função pura: depende apenas de seus parâmetros p/ gerar resultado
    valor = valor * fator       # não acessa nem modifica var. externa à função e retorna um valor
    return valor

def main():
    numero = int(input()) # recebido pelo usuário
    print("Resultado", multiplica(valor, numero))
    print("Resultado", multiplica(valor, numero))

if __name__ == "__main__":
    main()