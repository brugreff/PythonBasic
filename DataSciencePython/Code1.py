# Algoritmos Supervisionados - Regressão Linear 

# Série histórica fictícia de casos de dengue de uma cidade
# Predizer casos futuros(auxílio do alg supervisionado de regressão linear)

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

#### Pré-processamento ####
# Coleta e integração (carregar a planilha dentro do programa)
arquivo = pd.read_csv('DataSciencePython/dados_dengue.csv')

anos = arquivo[['ano']]
casos = arquivo[['casos']]

#### Mineração ####
# Criar objeto do tipo LinearRegression e atribuí-lo a uma variável
# Objeto irá treinar a equação reta gerada pela regressão
# Fit() - precisa dos parâmetros X e y p/ realizar o treinamento.
regr = LinearRegression()
regr.fit(X = anos, y = casos) # X: dados do treinamento/ y: respectivos resultados

# Objeton regr está pronto p/ ser utilizado p/ predizer os casos p/ anos futuros
# Utilização do métoto predict()
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