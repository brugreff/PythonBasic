# Tratamento de exceções e eventos
# Blocos try e except

try: # devem ser inseridas as instruções do fluxo normal do programa
    num = eval(input("Entre com um número inteiro: \n"))
    print(num)
except: # só será executado caso haja o levantamento de alguma exceção
    print("Entre com o valor numérico e não letras")

#Formato padrão de uso bloco try/except
#try:
#  Bloco 1
#except:
#  Bloco 2
#Instrução de fora do bloco try/except



