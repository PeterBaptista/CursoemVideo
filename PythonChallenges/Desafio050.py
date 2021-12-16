# Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar desconsidere-o.


print('Somas dos números pares!')

s = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        s += n

print(f'A somas dos números pares é \033[32m{s}')