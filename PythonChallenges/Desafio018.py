# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
valor = float(input('Digite um ângulo'))

rad = radians(valor)

sin = sin(rad)
cos = cos(rad)
tan = tan(rad)

print(f'O ângulo de {valor} tem o Seno de {sin:.2f}'
      f'\nO ângulo de {valor} tem o Cosseno de {cos:.2f}'
      f'\nO ângulo de {valor} tem a Tangente de {tan:.2f}')