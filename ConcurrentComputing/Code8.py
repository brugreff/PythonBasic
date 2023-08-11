# Programação concorrente - Threads

# a. Iniciar execução de duas Threads
# b. Primeira thread deve calcular o cubo de um nº
# c. Segunda thread deve calcular o quadrado de um nº
# d. Colocar a primeira e a segunda threads p/ esperar, respect., 3 e 2 segundos
# e. Informar a ordem de execução das threads

from time import sleep
from threading import Thread

def calcular_cubo(num, tempo_espera):
    print(f"\nCubo: {num * num * num}")
    sleep(tempo_espera)
    print('Conclusão da função calcular_cubo')

def calcular_quadrado(num, tempo_espera):
    print(f"\nQuadrado: {num * num}")
    print('Conclusão da função calcular_quadrado')

t1 = Thread(target=calcular_cubo, args=(5, 3))
t2 = Thread(target=calcular_quadrado, args= (5, 2))

t1.start()
t2.start()

t1.join()
t2.join()

print("A execução foi concluída!")