# Faça um programa que jogue par ou ímpar com o computador. o jogo só será
# interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.

from random import randint
from time import sleep
soma = cont = 0
while True:
    com = randint(0, 10)
    choice = int(input('Escolha um número entre 0 e 10: '))
    if choice > 10 or choice < 0:
        while choice < 0 or choice > 10:
            choice = int(input('\033[31mresposta inválida...\033[m escolha um número entre 0 e 10: '))
    choice2 = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    if choice2 not in 'PI':
        while choice2 not in 'PI':
            choice2 = str(input('\033[31mresposta inválida\033[m Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'\nVocê colocou {choice}')
    sleep(0.5)
    print(f'O computador colocou {com}')
    sleep(0.75)
    soma = com + choice
    print(f'A soma é igual a {soma}')
    sleep(1)
    if soma % 2 == 0 and choice2 == 'P':
        print('\033[32mVocê ganhou!!! MAIS UMA!\033[m')
        cont += 1
    elif soma % 2 != 0 and choice2 == 'I':
        print('\033[32mVocê ganhou!!! MAIS UMA!\033[m')
        cont += 1
    else:
        print('\033[31mVocê perdeu...\033[m')
        break
print(f'Você conseguiu ganhar {cont} vezes seguidas')
