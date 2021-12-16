# Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média.

nome = input('Nome do aluno ')
n1 = int(input(f'Primeira nota de {nome}: '))
n2 = int(input(f'Segunda nota de {nome}: '))

med = (n1 + n2)/2

print(f'A média de {nome} é igual a {med}')

