# Docstrings - string que serve como documentação de funções def. pelo dev

# Exemplo 
# Determinando o n-ésimo termo da seq de Fibonacci

def fibo(n):
    if n == 1 or n == 2: # declaração da Doctsring
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print(help(fibo)) # irá exibir a docstring - utilitário help() e função desejada como parâmetro