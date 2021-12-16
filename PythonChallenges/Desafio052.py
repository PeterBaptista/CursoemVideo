# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

print('Bem-vindo ao analisador de números primos!\n')
num = int(input('Digite um número: '))

n = 0
for c in range(1, num + 1):
    if num % c == 0 and c != num:
        n = c

n2 = 0
for c in range(-1, num + 1, -1):    # primo pode ser negativo
    if num % c == 0 and c != num:
        n2 = c


if n == 1 or n2 == -1:  # adicionei a possibilidade de ser negativo
    print(f'[{num}] \033[32mé um número primo')
else:
    print(f'[{num}] \033[31mnão é um número primo')
