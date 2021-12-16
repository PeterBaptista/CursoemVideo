# Melhore o jogo do Desafio028 onde o computador vai "pensar". Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

from random import randint
com = randint(0, 10)
print('-='*27)
print('\033[1;35mTente adivinhar que número o computador está pensando!\033[m')
print('-='*27)
tent = 0

acertou = False

while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    tent += 1
    if com == jogador:
        acertou = True
    else:
        if jogador < com:
            print(f'\033[34mmais...\033[m')
            print('\033[31mTente de novo:\033[m ')
        elif jogador > com:
            print('\033[34mmenos...\033[m')
            print('\033[31mTente de novo:\033[m ')

print('\033[32mVocê acertou!!!\033[m')
print(f'Foram necessárias {tent} tentativas')
