# Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.
# Ex.: Digite um número: 1834
# unidade: 4  dezena: 3  centena: 8  milhar: 1

num = (input('Digite um número na casa dos milhares: '))

mil = num[3]
cen = num[2]
dez = num[1]
uni = num[0]


print(f'UNIDADE: {uni}'
      f'\nDEZENA: {dez}'
      f'\nCENTENA: {cen}'
      f'\nMILHAR: {mil}')


