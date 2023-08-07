# Sequencia de Fibonacci

# Def: Dois primeiros termos são 1, a partir do 3º cada termo é a soma dos dois anteriores.
# 1, 1, 2, 3, 5, 8, 13, 21,...

# Possível implementação recursiva de função p/ determinar o n-ésimo termo

def fibo(n):
    if n == 1 or n == 2: # condições de parada
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2) # chamadas recursivas p/ calcular os dois termos anteriores
