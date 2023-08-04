# Variável global (alteração)
# Explicitar dentro de cada função que o nome x é referente a ela.
# Além de explicitar a ref. à variável global, as func1(x) e func2(x) não recebem mais os parâmetros de mesmo nome, que fazem ref. à var. global

# Exemplo alterando código de Code18.py

def func1():
    global x
    x = 10
    print(f'Função func1 - x = {x}')

def func2():
    global x 
    x  = 20
    print(f'Função func2 - x = {x}')


x = 0
func1()
func2() 
print(f'Programa principal - x = {x}')

# print() do progr. principal está depois da chamada à func2(x)
# var. global x, alterada na execução da func2(x), fica c/ valor 20 qd a execução volta ao programa principal