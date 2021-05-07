# IF
if 100 > 99:
  print("100 é maior que 99!")
  
  
# IF, ELSE
if 100 == 99:
  print("100 e 99 são iguais!")
else:
  print("100 é diferente de 99")
  
  
# IF, ELIF, ELSE
if 100 == 99:
  print("100 e 99 são iguais!")
elif 100 > 99:
  print("100 é maior que 99!")
else:
  print("100 é menor que 99!")
  
'''  
6 - Faça um Programa que peça dois números e imprima o maior deles.
7 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
8 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
9 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
10 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
  - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
  - A mensagem "Reprovado", se a média for menor do que sete;
  - A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

# desafio 6
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
if num1 > num2:
  print(f"O maior número é {num1}")
else:
  print(f"O maior número é {num2}")
  
  
# desafio 7
num1 = int(input(""))

if num1 > 0:
  print("O número é positivo!")
else:
  print("O número é negativo")
  
  
# desafio 8
letra = input("Digite a letra 'F' ou 'M': ")
if letra == 'F' or letra == 'f':
  print(f"F - Feminino")
elif letra == 'M' or letra == 'm':
  print(f"M - Masculino")
else:
  print(f"Sexo Inválido")
  
  
# desafio 9
letra = input("Digite uma letra: ")
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra =='u':
  print(f"A letra é uma vogal")
else:
  print(f"A letra é uma consoante")
  
  
# desafio 10
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media == 10:
  print(f"Aprovado com Distinção")
elif media >= 7 and media < 10:
  print(f"Aprovado")
else:
  print(f"Reprovado")
  
