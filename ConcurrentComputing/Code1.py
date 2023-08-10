# Criação de threads e processos
# Classe thread e process dos módulos threading e multiprocessing

# script principal.py
from threading import Thread
from multiprocessing import Process

def funcao_a(nome):
    print(nome)

def main():
    t = Thread(target=funcao_a, args=("Minha Thread",)) 
    t.start()           

    p = Process(target=funcao_a, args=("Meu Processo",))
    p.start()

if __name__ == '__main__':
    main()

# criação de uma thread p/ executar a função 'funcao_a', utilizando a classe thread (linha 12)
# parâmetros: funç a ser executada(target) e quais param. serão passados p/ essa funç(args)
# parâmetro args espera um iterável(cada elem será mapeado p/ um parâm. da função target)
# comando p/ a thread começar execução(linha 13): método start() do obj t do tipo thread
# mesma lógica na criação do processo(começo linha 15)
