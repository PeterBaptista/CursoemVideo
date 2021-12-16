# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

item = ('PEDRA', 'PAPEL', 'TESOURA')
com = randint(0, 2)

comchoice = item[com]

escolha = int(input('[0] PEDRA'
                    '\n[1] PAPEL'
                    '\n[2] TESOURA'
                    '\nEscolha uma opção: '))

if escolha > 2 or escolha < 0:
    print('\033[31mNúmero inválido')
    exit()

userchoice = item[escolha]

print('JO')
sleep(0.5)
print('Ken')
sleep(0.6)
print('PO!')
print('--='*12+'-')
print('[Você] \033[34m{}\033[m x \033[31m{}\033[m [Computador]'.format(userchoice, comchoice))
print('-=-'*12)

sleep(1.5)
if (escolha - com) == 1:
    print('\033[34mVocê ganhou!!')
elif (com - escolha) == 1:
    print('\033[31mVocê perdeu...')
else:
    print('\033[33mEmpate')





