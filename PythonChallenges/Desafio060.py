# Faça um programa que leias um número qualquer e mostre o seu fatorial.
# Ex.:
# 5! = 5x4x3x2x1 = 120

valor = int(input('Digite um número: '))
num = valor
num1 = valor
num2 = 0
fatorial = 1
while num1 != num2:
    num2 += 1
    if num1 != num2:
        fatorial = fatorial * (num1 * num2)
        num1 -= 1
    else:
        fatorial *= num1
mult = f'{valor} x '

while num != 0:
    num -= 1
    if num != 0 and num != 1:
        mult += f'{num} x '
    elif num == 1:
        mult += f'{num}'

print(f'{valor}! = {mult} = {fatorial}'
      f'\nO fatorial de {valor} é igual a {fatorial}')
