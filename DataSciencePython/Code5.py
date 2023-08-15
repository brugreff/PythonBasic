# Solução para estudar o comportamento de uma série temporal com Regressão Linear.

# Pacotes que vão ser trabalhados 
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Fornecendo os pontos 
x = np.array([5, 10, 15, 20, 25, 30]).reshape((-1, 1)) # reshape: irá reorganizar uma lista
y = np.array([6, 12, 14, 23, 17, 32])

# montar o modelo
model = LinearRegression().fit(x, y)

# Predict a Response and print it:
# Passando os parâmetros
y_pred = model.predict(x)
print('Dados do teste: ', y, sep='\n') # resultados do teste
print('Dados da predição: ', y_pred, sep='\n') # resultados que modelo gerou

# Utilizando matplotlib para imprimir 
plt.scatter(x, y, c="blue")
plt.plot(x, y_pred, c="red")
plt.legend(['Predição', 'Real'])
plt.show()