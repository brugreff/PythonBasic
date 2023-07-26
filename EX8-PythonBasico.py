# TIPOS NUMÉRICOS

# 1.Inteiro
print(type(1_000_000))

# 2.Float - ponto separando a parte inteira da parte decimal, ao invés da vírgula
print(type(50.0))

# Com operações apenas com elemenos int, a resposta será int
# Basta somente um  operando float para que a resposta retorne float
print(type(2+3+1))
print(type(2+3+1.0))

# Exponenciação
# Basta que a base seja float para que o resultado seja float
print(2**3)
print(type(2**3))
print(type(2.0**3))

#  A div de dois números inteiros nem sempre resulta em número inteiro
x = 5/2
print(x)

# Obtendo quociente inteiro e resto quando dois int são divididos
# Utilizar operadores //e %,  respectivamente

x = 21//2
print(x)

x = 21%2
print(x)

# 3.Complex
# x + yj (x:parte real, y:parte imaginária)
r = complex(2,5)
print(r)

w = 2 + 5j
print(type(w))

# 4.Bool(subdivisão dos int)
# Expressões booleanas - retornará True ou False 
print(2<3)
print(2>3)

# Operador not - inverte o valor booleano
print(not(2<3))

