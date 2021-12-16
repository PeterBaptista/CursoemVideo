# Escreva um programa que faça o computador "pensar"
# em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# obs.: O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep


num = randint(0, 5)

print('JOGO: Tente adivinhar o número que o computador está pensando!\n')

print('-=-'*20)
print('Vou pensar em número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)

chute = int(input('\nEm que número eu pensei? '))
print('...')


if chute < 0 or chute > 5:
    print('número inválido!')
else:
    if chute == num:
        sleep(1)
        print(f"Parabéns você acertou... Eu pensei em {num}! ＼(°o°)／")
    else:
        sleep(1)
        print(f'Você errou... '
              f'Eu pensei em {num} ¯\_(ツ)_/¯')

