def Potenciacao(x,y):
  return x**y
  
Potenciacao(2,2)


def Maiuscula(x):
  return x.upper()
  
Maiuscula("oi")

'''
16 - Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
17 - Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, 
se seu argumento for zero ou negativo.
18 - Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas 
expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
'''

# 16
def Func(a,b,c):
  return a+b+c 

Func(-12,-134,128)


# 17
def PositivoNegativo(valor):
  if valor > 0:
    return 'P'
  else:
    return 'N'

PositivoNegativo(450)


#18
def somaImposto(taxaImposto, custo):
  total_imposto = custo * (taxaImposto / 100)
  custo += total_imposto
  return custo

somaImposto(20, 250)
