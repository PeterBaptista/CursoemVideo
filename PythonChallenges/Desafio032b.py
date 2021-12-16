# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

print('-=-' * 15)
print('Bem vindo ao analisador de ano Bissexto!')
print('-=-' * 15)
year = int(input('\nQual ano você quer analisar? '))

if year == 0:
    year = date.today().year

else:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f'O ano {year} é BISSEXTO')
    else:
        print(f'O ano {year} não é BISSEXTO')
