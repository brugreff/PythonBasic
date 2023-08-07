# Função recursiva fatorial

# Definição: n!= 1(se n=0 ou n=1) / n!=n.[(n-1)!] (se n>=1)
#Implementação recursiva em Py - melhor opção

def fatorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n*fatorial(n-1)
    
# Implementação não recursiva em Py

def fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        for x in range(2, n + 1):
            fat = fat*x
        return fat
    
    
