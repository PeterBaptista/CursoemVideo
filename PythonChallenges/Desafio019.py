# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude-o, lendo o nome deles
# e escrevendo o nome do escolhido.

import random

alun1 = input('Qual o nome do primeiro aluno?')
alun2 = input('Qual o nome do segundo aluno?')
alun3 = input('Qual o nome do terceiro aluno?')
alun4 = input('Qual o nome do quarto aluno?')

sort = random.choice([alun1, alun2, alun3, alun4])

print(f'O aluno sorteado é {sort}')

