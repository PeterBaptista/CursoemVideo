# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. O programa vai perguntar
# o valor da casa, o salário do comprador e em quantos anos
# ele vai pagar.

#Calcule o valor da prestação mensal, sabendo
# que ela não pode exceder 30% do salário
# ou então o empréstimo será negado

from time import sleep

print('\033[33m-=-\033[m'*16)
print('\033[34mBem vindo ao analisador de empréstimo bancário!')
print('\033[33m-=-\033[m'*16)

casa = int(input('Qual o valor da casa que você quer financiar?\nR$'))
sal = int(input('Qual a quantia do seu salário?\nR$'))
ano = int(input('Em quantos anos você quer pagar?\n'))

prest = float(casa / (ano * 12))

sleep(0.5)
if prest > sal * 0.3:
    print('\033[31mO empréstimo foi negado!')
else:
    print(f'O valor da sua prestação mensal é \nR$\033[034m{prest:.2f}')