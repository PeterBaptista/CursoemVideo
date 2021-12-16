# Crie um programa que leia um frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.

nome = str(input('Digite um frase ou palavra:\n ')).strip().split()

let = len(''.join(nome))
nome2 = ''.join(nome).upper()
# APOSASOPA
# 012345678

p1 = ''
p2 = ''
if let % 2 != 0:
    for c in range(0, let//2 + 1):
        p = str(nome2[c])
        p1 += p
else:
    print('\033[31mNão é um palíndromo')
    exit()

if let % 2 != 0:
    for b in range((let - 1), (let // 2 - 1), -1):
        pp = str(nome2[b])
        p2 += pp

if p1 in p2:
    print('\033[32mA palavra ou frase digitada é um palíndromo!')
else:
    print('\033[31mA palavra ou frase digitada não é um palíndromo')


