# Laço while infinito
# Instrução aux - break: interrompe repetições
# Caso com vários loops alinhados

while True:
    print('Você está no primeiro laço.')
    opcao1 = input('Deseja sair dele? Digite SIM para isso.\n')
    if opcao1 == 'SIM':
        break # break do primeiro laço
    else:
        while True:
            print('Você está no segundo laço.')
            opcao2 = input('Deseja sair dele? Digite SIM para isso.\n')
            if opcao2 == 'SIM':
                break # break do segundo laço
        print('Você  saiu do segundo laço.')
print('Você saiu do primeiro laço.')