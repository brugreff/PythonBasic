# exemplo de def e chamada da função taxímetro

def taximetro(distancia, multiplicador = 1): # dois parâmetros formais
    largada = 3
    km_rodado = 2
    valor = (largada +  distancia * km_rodado) * multiplicador
    return valor #função retorna algum valor
# valor retornado é armazenado em uma variável do progr chamador
# ou utilizado como parêmetro p/ outra função

pagamento = taximetro(3.5)
print(pagamento)

# OBS: Retornar um valor é diferente de imprimir na tela.
#Função print() apenas imprime na tela(não retorna qualquer função def pelo usuário).