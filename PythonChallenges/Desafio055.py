# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

lista = []

for c in range(0, 5):
    peso = float(input('Qual seu peso em kg? '))
    lista += str(peso).split()

maior = 0
menor = 0
for b in range(0, 5):
    numlist = float(lista[b])
    if numlist > maior:
        maior = numlist
    if numlist != maior and menor == 0:
       menor = numlist
    if numlist < menor:
        menor = numlist

print(f'{menor}Kg é o menor peso')
print(f'{maior}Kg é o maior peso')
