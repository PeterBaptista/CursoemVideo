# Faça um programa que tenha um função chamada area(), que receba as dimensões
# de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    x = l * c
    print(f'A área do terreno {l}X{c} é igual a {x}m²')

a = float(input('Largura em metros: '))
b = float(input('Comprimento em metros: '))
area(a, b)