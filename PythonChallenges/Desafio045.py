# Crie um programa que faça o computador jogar Jokenpô com você

from random import randint
from time import sleep

print('\033[36mJOKENPÔ CONTRA O COMPUTADOR!\033[m')
escolha = int(input('Pedra: 1'
                    '\nTesoura: 2'
                    '\nPapel: 3'
                    '\n\nDigite um número: '))

if escolha < 1 or escolha > 3:
    print('\033[31mNúmero inválido')
    exit()

com = randint(1, 3)

print('-=-'*10)
if escolha == 1 and com == 1:
    print('(Você) - PEDRA x PEDRA - Computador')
elif escolha == 2 and com == 2:
    print('(Você) - TESOURA x TESOURA - Computador')
elif escolha == 3 and com == 3:
    print('(Você) - PAPEL x PAPEL - Computador')
elif escolha == 1 and com == 2:
    print('(Você) - PEDRA x TESOURA - Computador')
elif escolha == 1 and com == 3:
    print('(Você) - PEDRA x PAPEL - Computador')
elif escolha == 2 and com == 1:
    print('(Você - TESOURA x PEDRA - Computador')
elif escolha == 2 and com == 3:
    print('(Você) - TESOURA x PAPEL - Computador')
elif escolha == 3 and com == 1:
    print('(Você) - PAPEL x PEDRA - Computador')
elif escolha == 3 and com == 2:
    print('(Você) - PAPEL x TESOURA - Computador')

print('-=-'*10)

print('...')
sleep(1)

if (escolha == 1 and com == 1) or (escolha == 2 and com == 2) or (escolha == 3 and com == 3):
    print('\033[33mEmpatamos... ⊙﹏⊙')
elif (escolha == 1 and com == 2) or (escolha == 2 and com == 3) or (escolha == 3 and com == 1):
    print('\033[32mVocê ganhou... ಠ_ʖಠ')
elif (com == 1 and escolha == 2) or (com == 2 and escolha == 3) or (com == 3 and escolha == 1):
    print('\033[31mVocê Perdeu!!! (ﾉ◕ヮ◕)ﾉ*.✧')
