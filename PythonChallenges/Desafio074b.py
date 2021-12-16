# Crie um programa que vai gerar cinco números  aleatórios e colocar em um tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor
# e o maior valor que estão na tupla.

from random import randint

valores = randint(0, 10), randint(0, 10),\
          randint(0, 10), randint(0, 10), \
          randint(0, 10)
maior = menor = 0
print(f'Os valores sorteados foram: {valores}')
for pos, c in enumerate(valores):
    valor = valores[pos]
    if valor > maior or pos == 0:
        maior = valor
    if valor < menor or pos == 0:
        menor = valor
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
