# Recursividade com condição de parada

def regressiva(x):
    if x <= 0:           # condição de parada
        print('Acabou')
    else:
        print(x)
        regressiva(x-1) 

while True:
    x = input('Digite um número para x: ')
    try:                                     # teste
        x = int(x)                           
        break
    except:
        print("Você digitou algo não numérico, digite novamente")

regressiva(x)

# só vai parar a execução quando o input for numérico
