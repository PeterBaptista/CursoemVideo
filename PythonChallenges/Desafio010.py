# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.
# Considere
# US$1,00  = R$5,61

Real = float(input('Quantos Reais você tem na carteira? R$'))

dol = Real / 5.61
eu = Real / 6.31

print(f'Com {Real}R$ você pode comprar:'
      f'\n {dol:.2f} Doláres '
      f'\n     ou'
      f'\n {eu:.2f} Euros')