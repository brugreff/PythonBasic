# Calcular valor de uma compra (preço unitário R$10,00)

# Compra de até 10 unidades - sem descontos
# Compras entre 11 e 20 unidades - desconto de 10%
# Compras acima de 20 unidades - desconto de 20%

preco_unitario = 10.0
DESCONTO10  = 0.1
DESCONTO20 = 0.2
quantidade = eval(input('Digite a quantidade que irá comprar:'))
if(quantidade <= 10): # menor ou igual a 10
    valor_final = preco_unitario*quantidade 
elif (quantidade <= 20): #maior que 10 e menor ou igual a 20
    valor_final = preco_unitario*quantidade*(1-DESCONTO10)
else: #maior que 20
    valor_final = preco_unitario*quantidade*(1-DESCONTO20)

print(f'O valor final da compra é: {valor_final}')
