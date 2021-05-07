'''
https://www.techtudo.com.br/dicas-e-tutoriais/2019/02/aplicativo-para-identificar-plantas-por-foto-veja-como-usar-o-plantnet.ghtml
'''

# AQUISIÇÃO DE DADOS
# CARREGANDO LIBRARIES
#!pip install sklearn
from sklearn import datasets
iris = datasets.load_iris()
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html

help(datasets.load_iris)

# PRÉ-PROCESSAMENTO (PREPROCESSING) / ANÁLISE EXPLORATÓRIA
iris.feature_names

# DADOS QUE TEMOS
iris.data

# O QUE DEVEMOS PREVER? SEMPRE SEPARAR OS DADOS DAS RESPOSTAS!
iris.target
