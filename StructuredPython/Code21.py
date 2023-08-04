# Funções Recursivas 

# Recursividade - função que chama a si mesma 
# Exemplo

def regressiva(x):
    print(x)
    regressiva(x - 1)

x = int(input('Digite um número para x: '))
regressiva(x)

# Execução se repetirá infinitamente - loop infinito
# Resultando em um erro por falta de memória
# Motivo: não definição de uma condição de parada 