# Estrutura elif - permite o teste de 2 condições de forma sequencial

idade = eval(input('Informe a idade da criança:'))

if idade < 5:
    print('A criança deve ser vacinada contra a gripe.')
    print('Procure o posto de saúde  mais próximo.')
elif idade == 5:
    print('A vacina estará disponível em breve.')
    print('Aguarde as próximas informações.')
else:
    print('A vacinaçãovsó ocorrerá daqui a 3 meses.')
    print('Informe-se novamente neste prazo.')
print('Cuide da saúde sempre. Até a próxima.')