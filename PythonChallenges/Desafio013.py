# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

nome = input('Qual é o nome do funcionário? ')
valor = int(input('Qual é o salário dele?'))

aum = valor * 1.15

print(f"O salário de{nome} com um aumento de 15% é:\n{aum}R$")
