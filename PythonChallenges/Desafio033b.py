# Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor.

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

menor = a
maior = c

if c > a > b:
    menor = b
if b > c > a:
    maior = b
if b > a > c:
    maior = b
    menor = c
if a > b > c:
    maior = a
    menor = c
if a > c > b:
    maior = a
    menor = b

print('O maior valor é: {}'.format(maior))
print('O menor valor é: {}'.format(menor))

