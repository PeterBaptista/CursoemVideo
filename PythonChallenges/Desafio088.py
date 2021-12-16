# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
jogo = []
num = int(input('Digite quantos palpites você quer gerar: '))
cont = 0
print(f'===== SORTEANDO {num} JOGOS ======')
while True:
    com = randint(1, 60)
    if com not in jogo:
        jogo.append(com)
    if len(jogo) == 6:
        print()
        print(f'Jogo {cont + 1}: {sorted(jogo)}')
        jogo.clear()
        cont += 1
        sleep(1)
    if cont == num:
        break
print(f'{" < Boa Sorte > ":=^30}')
