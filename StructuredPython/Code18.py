# Variáveis locais

def func1(x):
    x = 10
    print(f'Função func1 - x = {x}')
# Função func1(x) recebe o parâmetro x, mas tem uma variável local = 10.

def func2(x):
    x = 20
    print(f'Função func2 - x = {x}')
# Funçõ func2(x) recebe o parâmentro x, mas tem uma variável local = 20.

# Programa principal
x = 0 # Variável global = 0.
func1(x) # func1(x) e func2(x) chamadas após atribuição da var.global de vlor nulo
func2(x) # ao executar, cada uma delas tem sua própria var. local(internamente)
print(f'Programa principal - x = {x}') 

# não há alteração na variável global mesmo com as atribuições das linhas 4 e 9.