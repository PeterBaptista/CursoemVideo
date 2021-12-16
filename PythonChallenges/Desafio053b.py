# Crie um programa que leia um frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]

if inverso == junto:
    print('\033[032mTemos um palíndromo!')
else:
    print('\033[31mA frase digitada não é um palíndromo!')