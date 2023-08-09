# Aplicando programação funcional

# Implementar uma solução p/  transformar todos os nomes da lista maiúsculo.
# Prog func - função

veiculos = ['avião', 'carro', 'navio', 'ônibus'] # lista em questão

f_maiuscula = lambda x: str.upper(x) # função que converte para maiúsculo
# função lambda - mt característica em progr. funcional
# parâmetro x

nomes_maiusculos = list(map(f_maiuscula, veiculos))
# aplica a função map
# dentro dela aplica a função 'f_maiúscula' p/ cada elemento na lista veículos
# poderia ser feito com for - progr. distribuída (mais ampla)
# elementos retornados da função: objetos
# list - transforma os novos elementos(objetos) em lista

print(f'nomes maiúsculos = {nomes_maiusculos}')