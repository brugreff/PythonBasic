# Ex 1 - Threads em Py

import threading
import time

# exemplo de funções sem parâmetros
def funcao():
    for i in range(3): # vai de 0 a 2
        print(i, 'Executando a thread!') # printa valor do índice e string
        time.sleep(1) # vai aguardar 1s

print('Iniciando o programa!')
threading.Thread(target=funcao).start() #chama a thread
print('Finalizando o programa!')