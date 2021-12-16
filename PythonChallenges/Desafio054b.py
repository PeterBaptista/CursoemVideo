# crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for person in range(1, 8):
    nasc = int(input(f'Em que ano a {person}ª nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

if totmaior == 1:
    print(f'uma pessoa é de maior e {totmenor} são de menor')
elif totmenor == 1:
    print(f'{totmaior} pessoas são de maior e uma é de menor')
elif totmenor == 0:
    print('7 pessoas são de maior e ninguém é de menor')
elif totmaior == 0:
    print('Ninguém é de maior e 7 pessoas são de menor')
else:
    print(f'{totmaior} são de maior e {totmenor} são de menor')

