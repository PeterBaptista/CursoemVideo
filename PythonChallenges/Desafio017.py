# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um retângulo,
# calcule e mostre o comprimento da hipotenusa.

# co = float(input('Qual a medida do cateto oposto? '))
# ca = float(input('Qual a medida do cateto adjacente? '))
#
# h = (co**2 + ca**2)**(1/2)
#
# print(f'A hipotenusa do seu triângulo é igual: {h}')

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = math.hypot(co, ca)

print(f'A hipotenusa desse triângulo é igual a {hi}')

print()