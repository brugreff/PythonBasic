# Programação Funcional

# Implementar solução p/ arredondar os valores da lista de números na mesma ordem da lista de precisão.

lista_numeros = [9.56783, 7.57568, 3.00914, 6.2321]
lista_precisao = [2, 2, 3, 3]

arredondamento = lambda x,y: round(x,y)
# função lambda pode receber mais de um parâmetro(neste caso, dois) 
# x: nº a ser arredondado / y: arredondamento
# retorna o valor arredondado

# mapeando os elementos das listas, função map()
resultado = list(map(arredondamento, lista_numeros, lista_precisao))
# duas listas como parâmetros
# transformar em lista

print(resultado)