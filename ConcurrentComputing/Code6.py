# Programação concorrente - Thread

# a. Iniciar a execução de uma thread
# b. Colocar a thread para esperar 2 segundos
# c. Informar o início e o final da execução da thread

from time import sleep
from threading import Thread


def tarefa(tempo_espera, mensagem):
    print(f'\nIniciando a tarefa {mensagem}')
    sleep(tempo_espera)
    print(f'Conclusão da tarefa {mensagem}')

# instanciando uma thread: função tarefa com parâmetros(args=)
thread = Thread(target=tarefa, args=(2, 'Thread em execução'))
thread.start() # início da execução

print('\nAguardando pela execução da Thread...')

thread.join()

print("A execução foi concluída")