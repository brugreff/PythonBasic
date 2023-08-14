# Algoritmos supervisionados - Algoritmo de Classificação
# Passa-se um conj de características sobre determinado item de uma classe
# Algoritmo compreende qual a classe de um item não mapeado

# Utilização de um dataset(conj de dados): Iris Dataset
# - Informações de 50 amostras de 3 diferentes classes de Flor de Íris 
# - No total: 4 características p/ cada amostra 
# Comprimento e largura(em cm) das sépalas e pétalas de rosas

# Treinando dois alg de classificação: árvore de decisão e máq. de vetor suporte(SVM)
# P/ montar dois classificadores de flores de Íris(implementaçãop destes fora deste escopo)

from sklearn.datasets import load_iris, fetch_kddcup99
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.svm import SVC

#### Pré-processamento ####
# Coleta e Integração - obtenção do dataset de flores
# função load_iris():retorna um obj p/ acessarmos as caract. das flores pelo atributo data e os rótulos, ou classes das flores pelo atributo target
iris = load_iris()

# separação das caract. das flores na variável características(lista com 150 itens)
# cada item contém uma outra lista com quatro elem.
# linha 28:separação dos rótulos ou classes na variável rótulo
# lista c/ 150 itens q variam entre 0, 1 e 2(classes da flor) - codificação categórico-numérica
caracteristicas = iris.data
rotulos = iris.target 

print("Características:\n", caracteristicas[:2])
print("Rótulos:\n", rotulos[:2])
print('#####################################################')

# Partição dos dados
# Permite verif. a qualidade do algoritmo de classif - particionar dados em treino e teste 
# Dados de treino: ajustar algoritmo
# Dados de teste: verif. a acurácia do algoritmo(compara os valores calc p/ os testes c/ os reais)
carac_treino, carac_teste, rot_treino, rot_teste = train_test_split(caracteristicas, rotulos)
# função train_test_slplit: recebe c/ parametro uma lista c/ as caract e uma lista c/ os rótulos
# - retorna 4 novas listas: treino, teste das caract, treino, teste dos rótulos

#### Mineração ####

#### --------- Árvore de Decisão --------- ####
# Treino de um alg de classif. com os dados de treino
# Classificador DecisionTree, tendo como parâm a profundidade máx da árvore
arvore = DecisionTreeClassifier(max_depth=2)
arvore.fit(X = carac_treino, y = rot_treino)

# Método predict do obj árvore, argumento: caract. p/ teste 
# Resultado: lista c rótulos preditos - utilizado p/ a função accuracy_score(calc. a acurácia do classificador)
# - compara resltados preditos c/ reais 
rot_preditos = arvore.predict(carac_teste)
acuracia_arvore = accuracy_score(rot_teste, rot_preditos)

#### -------- Máquina de Vetor Suporte -------- ####
# Treino de um alg. de classif usando o SVM(pela classe SVC-SUPPORT VECTOR CLASSIFICATION)
# Utilização dos valores padrão do contrutor p/ o classificador
clf = SVC()
clf.fit(X = carac_treino, y = rot_treino)

rot_preditos_svm = clf.predict(carac_teste)
acuracia_svm = accuracy_score(rot_teste, rot_preditos_svm)

#### Pós-processamento ####
# Imprimir a acurácia de cada classificador
print("Acurácia Árvore de Decisão: ", round(acuracia_arvore, 5))
print("Acurácia SVM: ", round(acuracia_svm, 5))
print('###################################################')

# Representação textual da árvore(função export_text)
r = export_text(arvore, feature_names = iris['feature_names'])
print("Estrutura da árvore")
print(r)