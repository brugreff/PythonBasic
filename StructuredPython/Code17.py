# Procedimentos e Funções
# Proced - não retornam valores / Funç - retornam valores

# Em Py: as funções podem ser def. sem retornar qlqr valor, tendo comportamento de procedimento.

def func1(x):
    x = 10
    print(f'Função func1 - x = {x}')

def func2(x):
    x = 20
    print(f'Função func2 - x = {x}')


x = input("Digite um número: ")
func1(x)
func2(x)
print(f'Programa principal - x = {x}')

# As funções "func1(x)" e func2(x) não possuem retorno.
# Comportamento de procedimento