# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para vaigens mais longas.

print('Bem vindo à calculadora de preço de viagens!\n')
km = int(input('Qual a distância da viagem em Km?'))

if km <= 200:
    print(f'\nO preço da viagem é R${km*0.5:.2f}')
else:
    print(f'\nO preço da viagem é R${km*0.45:.2f}')
