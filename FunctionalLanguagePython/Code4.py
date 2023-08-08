# Funções lambda - como as funções anônimas são chamadas em Python
# Sempre retornam o valor da expressão automaticamente 
# Def. sem identificador e normalmente usadas como argumentos p/ outras funções(de ordem superior)

# Sintaxe utilizada:
# lambda argumentos: expressão

# Inicia-se c/ a palavra lambda, seguida de uma seq de argum. separados por vírgula, dois pontos e uma expr. de uma linha

# Exemplo 
# Função para multiplicar dois nº:
def multiplicar(a, b):
    return a*b

# Função lambda equivalente:
lambda a, b: a*b

# a palavra return não é necessária
# expressão a*b é retornada automaticamente 
# func lambda: podem ser armazenadas em variáveis p/ depois serem chamadas como uma func qualquer
