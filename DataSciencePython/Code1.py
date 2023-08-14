# Algoritmos Supervisionados - Regressão Linear 

# Série histórica fictícia de casos de dengue de uma cidade
# Predizer casos futuros(auxílio do alg supervisionado de regressão linear)

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

#### Pré-processamento ####
# Coleta e integração 
arquivo = pd.read_csv('DataSciencePython/dados_dengue.csv')

anos = arquivo[['ano']]
casos = arquivo[['casos']]

#### Mineração ####
regr = LinearRegression()
regr.fit(X = anos, y = casos)

ano_futuro = [[2018]]
casos_2018 = regr.predict(ano_futuro)

print('Casos previstos para 2018 ->', int(casos_2018))

#### Pós-processamento ####
plt.scatter(anos, casos, color='black')
plt.scatter(ano_futuro, casos_2018, color='red')
plt.plot(anos, regr.predict(anos), color='blue')

plt.xlabel('Anos')
plt.ylabel('Casos de dengue')
plt.xticks([2018])
plt.yticks([int(casos_2018)])

plt.show()