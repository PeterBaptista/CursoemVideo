# Faça um programa que calcule a soma entre
# todos os números ímpares que são múltiplos
# de 3 e que se encontram no intervalo de
# 1 até 500.

num = 0
cont = 0
for c in range(0, 501, 3):
    if c % 2 != 0:
        num += c
        cont += 1

print(f'A soma dos \033[34m{cont}\033[m números ímpares, múltiplos de 3, entre 0 e 500'
      f'\né igual a \033[33m{num}')


