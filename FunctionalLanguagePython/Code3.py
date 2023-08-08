# Funções de ordem superior - funções que aceitam outras funções (Como parâmetros ou que retornem uma função)
# Uso comum em programação funcional 

# Exemplo - script funcao5.py
# Criação da função de ordem sup. 'multiplicar_por' - criar e retornar novas funções 
# Funç. chamada c/ determinado multiplicador como argumento
# Retorna uma nova funç. multiplicadora por aquele multiplicador(Que tem como parâmetro o nº a ser multiplicado(multiplicando))

def multiplicar_por(multiplicador): 
    def multi(multiplicando): # def da func multi dentro da func "multiplicar_por"
        return multiplicando * multiplicador # func multi espera o parâmetro multiplicando(q será multiplicado pelo multiplicador)
    return multi # passado como parâmetro para a função 'multiplicar_por'

def main():
    multiplicar_por_10 = multiplicar_por(10) 
    print(multiplicar_por_10(1))
    print(multiplicar_por_10(2))

# Chamando a func multiplicar_por c/ argumento 10(linha 17)
# - definimos a func interna multi como: 

# def multi(multiplicando):
#   return multiplicando*10

# Func é retornada e armazenada na variável 'multiplicar_por_10'
# - passa nº como argumento, o multiplicando, p/ ser multiplicado por 10(linha 18 e 19) - produzindo resultados 10 e 20
 
    multiplicar_por_5 = multiplicar_por(5)
    print(multiplicar_por_5(1))
    print(multiplicar_por_5(2))

# Func multiplicar_por c/ argumento 5(linha 28) - mesma lógica anterior 


# Convenção usada para organizar e executar um programa adequadamente 
if __name__ == "__main__": 
    main()

# 'if __name__ == "__main__":' - verifica se o prog está sendo executado como prog principal
# *'__name__' - var. interna que o Py define automaticamente, indicando o contexto de execução do script
# 'main()' - chamada à funç. main, definida anteriormente no código(linha 13)