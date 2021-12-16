# Crie um programa que leia um frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite um frase: ')).strip().upper().split()
junto = ''.join(frase)
inverso = junto[::-1]

print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('\033[32mTemos um palíndromo!')
else:
    print('\033[31mNão é um palíndromo!')
