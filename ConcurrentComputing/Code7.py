# Programação concorrente - Thread

# a. Iniciar execução de duas Threads.
# b. Colocar a primeira e a segunda threads para esperar, respectivamente, 3 e 2 segundos.
# c. Informar a ordem de execução das threads.

from threading import Thread
from time import sleep

def tarefa(tempo_espera, nome_tarefa):
    print(f'Iniciando a tarefa {nome_tarefa}')
    sleep(tempo_espera)
    print(f'Conclusão da tarefa {nome_tarefa}')

# estanciando as duas threads
# alvo: função tarefa com os parâmetros tempo_espera e nome_tarefa
t1 = Thread(target=tarefa, args=(3, 'A'))
t2 = Thread(target=tarefa, args=(2, 'B'))

# executar threads
t1.start()
t2.start()

t1.join() # espera até completar a exec. da thread 1
t2.join() # espera até completar a exec. da thread 2

print("A execução foi concluída") 