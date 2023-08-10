# Ex 2 - Threads em Py

import threading
import time

# exemplo de função com parâmetros
def funcao(mensagem):
    for i in range(3):
        print(i, mensagem)
        time.sleep(1)

print('Iniciando o programa!')
x = threading.Thread(target=funcao,args=('Executando',))
x.start()
print('Finalizando o programa!')