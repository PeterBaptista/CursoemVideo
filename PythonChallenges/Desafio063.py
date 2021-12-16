# Escreva um programa que leia um número n inteiro qualquer e
# mostre na tela os n primeiros elementos de um Sequência de Fibonacci.
# Ex.:
# 0 → 1 → 2 → 3 → 5 → 8
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
t3 = 0
cont = 3

print(f'{t1} → {t2} ', end='')

while cont <= n:
    t3 = t1 + t2
    print(f'→ {t3} ', end='')
    t1 = t2
    t2 = t3
    cont += 1
