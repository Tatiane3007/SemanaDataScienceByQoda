'''
R MARKDOWN + Shiny https://r4ds.had.co.nz/

--- AMBIENTE DE DESENVOLVIMENTO ---

  - ANACONDA em https://www.anaconda.com/distribution/

  - Efetue download/instalação do R em https://cloud.r-project.org/

  - Efetue download/instalação do RStudio(IDE para programarmos com R) em https://www.rstudio.com/products/rstudio/download/

  - Novo projeto R com Colab https://colab.research.google.com/notebook#create=true&language=r
'''

'''
# --------------------------------------- Declarando variáveis, comentando código e printando na tela: --------------------------------------------------------
  Declare variáveis com = ou <-
  Utilize # para comentar linhas
  Utilize print() para executar na tela
  Utilize readline(prompt=”…”) para receber texto(inputs)
'''

# Você pode declarar variáveis utilizando "=" ou "<-"
x = "Hello Qoda!"
y <- "Hello Qoda!"


z = readline("Qual é o seu nome?")
print(z)



'''
# --------------------------------------- Tipos de Dados(básicos) ------------------------------------------------------------------------------------------------
  Character(“Texto”) Neste tipo inserimos caracteres, podendo ser números, textos, símbolos…;
  
  Integer (1L) Integer se refere a números inteiros e utilizamos o “L” para determina-lo, diferente do Numeric, onde os números são decimais: 1.0 e não 1;
  
  Numeric (7.25) Números decimais, mesmo que declarando-os como 12, o sistema retornará 12.0, por exemplo.
  
  Logical (T/F ou TRUE/FALSE) Tipo de dado com retorno TRUE ou FALSE, assim como T ou F. TRUE quando atendidas as condições e 
    FALSE quando não atendidas. Nos aprofundaremos logo logo neste tipo de dado: tenha paciência.
'''

caract = "Texto caractere"
class(caract) 
#retorna 'character'


inteiro = 15L
class(inteiro) 
#retorna 'integer'


num = 15
class(num)
#retorna 'numeric'


logic = T
class(logic)
#retorna 'logical'



# --------------------------------------- Estruturas de Dados ------------------------------------------------------------------------------------------------

# VETOR 

vec = 3
is.vector(vec) #Retorna TRUE


# Para adicionar diversos elementos em 1 vetor, use c()
vec = c(1,2,3,"texto")
class(vec) #retorna character pois todos elementos serão do mesmo tipo





# --------------------------------------- LISTA ---------------------------------------------------------------------------------------------

x = c("texto1","texto2")
y =  c(1,2,3)
z = c(T,F,T)
lista = c(x,y,z) 
lista
#retorna: 'texto1' 'texto2' '1' '2' '3' 'TRUE' 'FALSE' 'TRUE'




# --------------------------------------- MATRIZ  ---------------------------------------------------------------------------------------------

mat = matrix(c(1,2),nrow=1,ncol=2,byrow = TRUE) 
#nrow se refere ao número de colunas e ncol se refere ao número de linhas
#byrow insere os elementos dentro de linhas quando TRUE ou em colunas, quando FALSE
#retorna: 1 2
mat



# --------------------------------------- DATAFRAME (estrutura para armazenar em forma de tabela)  ----------------------------------------------------------

x = data.frame(nome = c("Ana","Weber","Aquiles"),
               idade = c(24L,27L,2L),
               salario = c(12000,0,0))
#nrow(x) #retorna número de linhas do dataframe
#ncol(x) #retorna número de colunas do dataframe
dim(x) #retorna número de linhas e colunas



# --------------------------------------- CONDICIONAIS  ---------------------------------------------------------


if (3 > 0) {
 
    print("3 é maior que 0")
 
}



if (3 == 0) {
 
  print("3 = 0")
 
} else {
 
    print("3 não é igual a 0")
 
}


a = 1
b = 2
ifelse(a>0,"A maior que 0","A menor que 0")
#retorna A maior que 0



# --------------------------------------- FUNÇÕES  ---------------------------------------------------------

# FUNÇÕES R BASE
x = c(1,2,3,4,5,6,7,8,9,10)
#sd(x) #desvio padrão
#mean(x) #média
#head(iris) #primeiras linhas dataframe
#tail(iris) #ultimas linhas dataframe
file.choose() #abre pasta para caminho de arquivos


raizquadrada = function(x) {
  return(x*x)
}
raizquadrada(23412341)



# --------------------------------------- PACOTES  ---------------------------------------------------------

#Instala pacote
install.packages("ggplot2", dependencies=TRUE)

# Carrega pacote para ser utilizado no código
library(ggplot2)
