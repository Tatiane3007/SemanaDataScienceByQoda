# FOR range
#  start, stop, step
# começa em 0, mas não conta o último elemento
for x in range(0,1):
  print(x)
  
  
# FOR
palavra = 'amanhã'
for letra in palavra:
  print(letra)
  

# WHILE
num = 0
while num < 100:
  print(num)
  num += 1
  
  
'''
11 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
12 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
13 - Faça um programa que leia e valide as seguintes informações:
      Nome: maior que 3 caracteres;
      Idade: entre 0 e 150;
      Salário: maior que zero;
      Sexo: 'f' ou 'm';
      Estado Civil: 's', 'c', 'v', 'd';
14 - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa 
de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, 
mantidas as taxas de crescimento.
15 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''

# 11
num1 = int(input("Digite um valor entre 0 e 10: "))
while num1 < 0 or num1 > 10:
  print("Valor inválido!")
  num1 = int(input("Errado! Digite um valor entre 0 e 10: "))
  

# 12
nome = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")
while senha == nome:
  print("Erro! A senha não pode ser igual ao nome de usuário!")
  nome = input("Digite a senha: ")
print("Senha aceita")


# 13
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
sal = float(input("Digite seu salário: R$ "))
sexo = input("Digite seu sexo 'f' - feminino ou 'm' - masculino: ")
estciv = input("Digite seu estado civil 's' - solteiro(a), 'c' - casado(a), 'v' - viúvo(a), 'd'- divorciado(a)")


while len(nome) < 3:
    print("O nome deve ter mais que 3 caracteres!")
    nome = input("Digite seu nome: ")
while idade < 0 or idade > 150:
    print("Idade deve ser entre 0 e 150!")
    idade = int(input("Digite sua idade: "))
while sal < 0:
    print("Salário deve ser maior do que 0!")
    sal = float(input("Digite seu salário: R$ "))
while sexo != "f" and sexo != "m":
    print("Sexo deve ser 'f' ou 'm'!")
    sexo = input("Digite seu sexo 'f' - feminino ou 'm' - masculino: ")
while estciv != "s" and estciv != "c" and estciv != "v" and estciv != "d":
    print("Estado civil deve ser 's' 'c' 'v' ou 'd'!")
    estciv = input("Digite seu estado civil 's' - solteiro(a), 'c' - casado(a), 'v' - viúvo(a), 'd'- divorciado(a)")
print("Todos os dados aceitos com sucesso!")


# 14
a = 80000
b = 200000
anos = 0

while a < b:
    txa = int(0.03 * a)
    a += txa
    txb = int(0.015 * b)
    b += txb
    anos += 1

    print(f"txa ---> {txa}")
    print(f"txb ---> {txb}")

    print(f"A: {a}")
    print(f"B: {b}")
    print(f"{anos} anos")
    print(f"\n")
    
    
# 15
a = int(input("Informe a população A: "))
while a <= 0:
    print(f"Erro! o valor precisa ser maior que 0!")
    a = int(input("Informe a população A: "))

txa = int(input("Informe a taxa de crescimento da população A: "))
while txa <= 0:
    print(f"Erro! o valor precisa ser maior que 0!")
    txa = int(input("Informe a taxa de crescimento da população A: "))

b = int(input("Informe a população B: "))
while b <= 0:
    print(f"Erro! o valor precisa ser maior que 0!")
    b = int(input("Informe a população B: "))

txb = int(input("Informe a taxa de crescimento da população B: "))
while txb <= 0:
    print(f"Erro! o valor precisa ser maior que 0!")
    txb = int(input("Informe a taxa de crescimento da população B: "))

anos = 0

while a < b:
    aum_a = (txa / 100) * a
    a += aum_a

    aum_b = (txb / 100) * b
    b += aum_b

    anos += 1

    print(f"A: {a}")
    print(f"B: {b}")
    print(f"{anos} anos")
    print(f"\n")
