# Escreva um programa que leia um valor em METROS
# e o exiba convertido em CENTÍMETROS e MILÍMETROS.

valor = float(input('Digite um valor em metro: '))

cm = valor * 100
mm = valor * 1000
km = valor / 1000
dam = valor / 10
hm = valor / 100

print(f'Quilômetro:{km}km\nHectômetro: {hm}hm\nDecâmetro: {dam}dam'
      f'\nMetro: {valor}m '
      f'\nCentímetro: {cm}cm \nMilímetros {mm}mm'
      f'\n')
