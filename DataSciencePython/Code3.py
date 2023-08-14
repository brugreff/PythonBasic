# Algoritmo não supervisionado - Agrupamento 
# Reunir objetos de uma coleção com algum grau de afinidade 
# Usa-se uma função p/ maximizar a similaridade de obj do mesmo grupo e minimizar entre elem de outros grupos

# Utilizando algoritmo k-medias: gerar grupos a partir do dataser de Flor de Íris
# Não utiliza rótulos(alg automaticamente separa as amostras em grupos)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

#### Pré-processamento ####
# Coleta e Integração
iris = load_iris()
caracteristicas = iris.data

#### Mineração ####
# Treinar o alg de agrupamento k-medias com características das flores 
# - instancia da classe KMeans: parâmetro(nº de grupos ou classes q desejamos que o alg encontre - clusters)
grupos = KMeans(n_clusters=3, n_init=10) # 3: sabe-se que são três classes de flor 
grupos.fit(X = caracteristicas)
labels = grupos.labels_ # indice do grupo ao qual cada amostra pertence 

#### Pós-processamento ####
# Utilização da biblioteca Matplotlib: exibir os dois gráficos(obj do mesmo grupo possuem mesma cor)
fig = plt.figure(1)
ax = fig.add_subplot(121, projection='3d') # Cria um subplot 3D
ax.set_xlabel('Comprimento Sépala')
ax.set_ylabel('Largura Sépala')
ax.set_zlabel('Comprimento Pétala')
ax.scatter(caracteristicas[:, 0], caracteristicas[:, 1], caracteristicas[:, 2], c=grupos.labels_, edgecolor ='k')

target = iris.target
fig = plt.figure(2)
ax = fig.add_subplot(122, projection='3d') # Cria outro subplot 3D
ax.set_xlabel('Comprimento Sépala')
ax.set_ylabel('Largura Sépala')
ax.set_zlabel('Comprimento Pétala')
ax.scatter(caracteristicas[:, 0], caracteristicas[:, 1], caracteristicas[:, 2], c=target, edgecolor ='k')

plt.show()