'''
https://www.kaggle.com/uciml/sms-spam-collection-dataset
'''

# ================================ Aquisição de dados =======================================================

# BIBLIOTECAS
import random
import spacy
import pandas as pd
import seaborn as sns
from spacy.util import minibatch
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from matplotlib import pyplot as plt

# dados
data_path = "https://raw.githubusercontent.com/qodatecnologia/spam-data/main/spam-data.csv"
data = pd.read_csv(data_path)
print(data.head())


# ================================ ANÁLISE EXPLORATÓRIA DE DADOS =======================================================

data = pd.read_csv(data_path)
observations = len(data.index)
print(f"Tamanho do Dataset: {observations}\n")
print(data['v1'].value_counts())
print()
print(data['v1'].value_counts() / len(data.index) * 100.0)



# ================================ PASSO 3: PIPELINE SPACY =======================================================

'''
Para construir modelos com Spacy, você pode carregar os modelos de pipeline existentes ou criar um modelo vazio 
e adicionar as etapas de modelagem. Na 1ª linha, criamos o modelo vazio com spacy e passamos o idioma do dataset 
que é o inglês (en). Nas próximas linhas, estamos criando um pipeline dizendo que precisamos que esse modelo 
execute a classificação do texto. Utilizamos a arquitetura “bow” que, basicamente, executa “bag of words”. 
Em seguida, estamos adicionando o pipeline “text_cat” criado ao nosso modelo vazio. Nesta fase estamos tendo 
um modelo e estamos dizendo que este modelo deve realizar a classificação do texto utilizando a abordagem “bow”. 
Em seguida, estamos adicionando as classes target spam e ham ao modelo de categorização de texto criado. Não 
estamos executando nenhuma técnica de pré-processamento de texto com NLP pois foge do escopo deste tutorial e 
principalmente por recebermos o dataset já tratado: o que é raro no mundo real.
'''

# Criamos um modelo vazio com o idioma do dataset
nlp = spacy.blank("en")

# Criamos agora um classificador de texto com classes exclusivas + arquitetura "bow" 
text_cat = nlp.create_pipe(
              "textcat",
              config={
                "exclusive_classes": True,
                "architecture": "bow"})

# Adicionamos o classificador a nosso modelo vazio
nlp.add_pipe(text_cat)

# Adicionamos as "classes exclusivas"
text_cat.add_label("ham")
text_cat.add_label("spam")


# ================================ TREINO/TESTE =======================================================

'''
Vamos dividir os dados carregados em TREINO/TESTE.

Conjunto de dados de treinamento: para treinar o modelo de categorização de texto. Conjunto de dados 
de teste: para validar o desempenho do modelo.

Para dividir os dados em 2 conjuntos de dados, usaremos o train_test_split do scikit learn, de forma 
que os dados de teste representem 33% dos dados carregados.
'''

x_train, x_test, y_train, y_test = train_test_split(
      data['v2'], data['v1'], test_size=0.33, random_state=7)



'''
Ao contrário dos outros modelos do scikit-learn, você não pode passar o destino como uma única coluna 
para o spacy, precisamos criar explicitamente os destinos como uma lista booleana de True/False. Como 
para cada texto de e-mail, o target é True. Criamos onehot encoding para categorias target(o que 
queremos prever), onde estamos criando dois rótulos booleanos(True/False) e atribuindo True para o 
rótulo real e False para o outro rótulo. Agora temos features e targets para treinar o modelo, mas 
primeiro precisamos combinar as features e os targets em um único conjunto de dados para construir o 
modelo de classificação de e-mail. Estamos pegando as features (texto do e-mail), convertendo rótulos 
de treino (booleanos) e juntando-os usando o método zip, a mesma abordagem que estamos aplicando para 
conjuntos de dados de treinamento e teste.
'''

train_lables = [{'cats': {'ham': label == 'ham',
                          'spam': label == 'spam'}}  for label in y_train]

test_lables = [{'cats': {'ham': label == 'ham',
                      'spam': label == 'spam'}}  for label in y_test]

# Spacy model data
train_data = list(zip(x_train, train_lables))
test_data = list(zip(x_test, test_lables))



'''
Para cada época, estamos embaralhando os dados usando o método de embaralhamento “shuffle” e, 
em seguida, criando os batches(lotes de treinamento).

Para cada lote atualizamos o modelo usando o otimizador e, no final, capturamos as loss functions.

model: modelo vazio já criado
train data: dados de treino
optimizer: Otimizador
batch size: Tamanho dos batches
epochs: épocas de treinamento
'''

def train_model(model, train_data, optimizer, batch_size, epochs=10):
    losses = {}
    random.seed(1)

    for epoch in range(epochs):
        random.shuffle(train_data)

        batches = minibatch(train_data, size=batch_size)
        for batch in batches:
            # Split batch into texts and labels
            texts, labels = zip(*batch)

            # Update model with texts and labels
            model.update(texts, labels, sgd=optimizer, losses=losses)
        print("Loss: {}".format(losses['textcat']))

    return losses['textcat']


optimizer = nlp.begin_training()
batch_size = 5
epochs = 10

# Treinar!
train_model(nlp, train_data, optimizer, batch_size, epochs)



# ================================ PASSO 5: PREDIÇÕES =======================================================

'''
Para o texto de sms/e-mail abaixo, a saída real é “ham” e nosso modelo está tendo alta probabilidade 
de quase 99% para ham e 1% para spam. O que significa que nosso modelo está prevendo o texto do 
e-mail corretamente.
'''

print(train_data[0])
sample_test = nlp(train_data[0][0])
print(sample_test.cats)



'''
A função abaixo “get_predictions” usa dois parâmetros, um é o modelo e o outro é o texto da sms. 
Na 3ª linha da função, o texto é tokenizado e, em seguida, dividimos o conteúdo da sms e armazenamos 
em documentos. Nas próximas linhas chamamos o método “textcat” que criamos, usando o objeto textcat 
para prever a classe de spam ham/spam. As Pontuações basicamente fornecem as probabilidades para 
ambas as classes. Para identificar a classe de rótulo, estamos pegando a probabilidade máxima usando 
o argmax, então estamos retornando as previsões.
'''

def get_predictions(model, texts):
    # Tokenizar
    docs = [model.tokenizer(text) for text in texts]

    # textcat para verificar os scores
    textcat = model.get_pipe('textcat')
    scores, _ = textcat.predict(docs)

    # Mostramos os scores mais altos com argmax
    predicted_labels = scores.argmax(axis=1)
    predicted_class = [textcat.labels[label] for label in predicted_labels]

    return predicted_class



# ================================ AVALIAÇÃO DO MODELO =======================================================

'''
Para problemas supervisionados de classificação, podemos/devemos utilizar acurácia e a matriz de confusão.
'''

# ACURÁCIA
train_predictions = get_predictions(nlp, x_train)
test_predictions = get_predictions(nlp, x_test)

train_accuracy = accuracy_score(y_train, train_predictions)
test_accuracy = accuracy_score(y_test, test_predictions)

print(f"Train accuracy: {train_accuracy}")
print(f"Test accuracy: {test_accuracy}")


# MATRIZ DE CONFUSÃO TREINO
print("TREINO:")
cf_train_matrix = confusion_matrix(y_train, train_predictions)
plt.figure(figsize=(10,8))
sns.heatmap(cf_train_matrix, annot=True, fmt='d')


# MATRIZ DE CONFUSÃO TESTE
print("TESTE:")
cf_test_matrix = confusion_matrix(y_test, test_predictions)
plt.figure(figsize=(10,8))
sns.heatmap(cf_test_matrix, annot=True, fmt='d')
