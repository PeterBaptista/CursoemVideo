# Desenvolva um programa que leia o primeiro termo e a razão de um PA.
# No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
aa1 = a1
print('\nOs 10 primeiros termos da \033[34mProgressão Aritmética:\033[m')
for c in range(0, 10):
    print(a1, end=" → ")
    a1 += raz

print('...')
print('\nOs 10 primeiros termos da \033[31mProgressão Geométrica:\033[m')

for c in range(0, 10):
    print(aa1, end=" → ")
    aa1 *= raz
print('...')