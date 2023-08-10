# Ex 3 - Threads em Py

import threading
import time

# sincronizando threads
ls = [] # declaração de uma lista

# declaração de duas funções(ambas têm n como parâmetro)
def contador1(n):
    for i in range(1, n + 1):
        print(i)
        ls.append(i)
        time.sleep(0.4)

def contador2(n):
    for i in range(6, n + 1):
        print(i)
        ls.append(i)
        time.sleep(0.5)

# criando 1ª Thread, chamando func contador1, passando o 5 como parâmetro(vai de 1 até 5)
x = threading.Thread(target=contador1,args=(5,))
x.start()

# para que execute toda uma thread e depois execute a outra thread
# após sua finalização, irá printar a lista
x.join()

# criando 2ª Thread, chamando func contador2, passando o 10 como parâmetro(vai de 6 até 10)
y = threading.Thread(target=contador2,args=(10,))
y.start()

# execução da Thread pode não seguir uma sequência como deveria (não executa na sequência correta)
# utilização do join()
# faz com que as duas threads (x e y) executem e somente depois irá executar o print(ls)
x.join()
y.join()

print (ls)