#
nome = input("Qual é o seu nome? ")
print(f"Hello {nome}")

'''
1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.
2 - Faça um Programa que peça um número e então mostre a mensagem "O número informado foi [número]."
3 - Faça um Programa que peça dois números e imprima a soma.(+)
4 - Faça um Programa que peça as 3 notas e mostre a média.(/)
5 - Faça um Programa que converta metros para centímetros.(/)
'''

# 1
print("Alo mundo")

# 2 
numero = input("Digite um número: ")
print(f"O número informado foi {numero}")

# ex. 3
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print(f"A soma dos números é: {n1 + n2}")

# ex. 4
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é: {media}")

# ex. 5
m = int(input("Digite a distância em metros: "))
c = m * 100
print(f"A distância em centímetros é: {c}")
