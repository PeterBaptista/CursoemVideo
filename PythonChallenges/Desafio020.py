 # O mesmo professor do desafio anterior quer sortear a ordem de apresentação
 # de trabalhos dos alunos. Faça um programa que leia o nome dos quatro
 # alunos e mostre a ordem sorteada

from random import shuffle

alun1 = input('Nome do primeiro aluno: ')
alun2 = input('Nome do segundo aluno: ')
alun3 = input('Nome do segundo aluno: ')
alun4 = input('Nome do segundo aluno: ')

deck = [alun1, alun2, alun3, alun4]
shuffle(deck)

print(f'A ordem dos alunos é: {deck}')
