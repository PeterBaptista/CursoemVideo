# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
print(f'Os divisores de \033[31m{num}\033[m são:')

tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[34m{c}\033[m', end=' ')
        tot += 1

tot2 = 0
for c in range(-1, num - 1, -1):
    if num % c == 0:
        print(f'\033[34m{c}\033[m', end=' ')
        tot2 += 1

if tot == 2 or tot2 == 2:
    print(f'\nO número {num} é primo')
else:
    print(f'\nO número {num} não é primo')

