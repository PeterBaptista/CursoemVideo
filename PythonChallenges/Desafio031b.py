# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para vaigens mais longas.

km = int(input('Qual a distância da viagem? R$'))

valor = km * 0.50 if km <= 200 else km * 0.45
print('O preço da viagem será R${:.2f}'.format(valor))