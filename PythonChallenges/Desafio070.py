# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.
mais1000 = cont = maisbarato = total = 0
produtobarato = ''
while True:
    cont += 1
    produto = str(input('Qual o nome do produto? '))
    price = float(input('Qual o preço dele? R$'))

    if price > 1000:
        mais1000 += 1
    if price < maisbarato or cont == 1:
        maisbarato = price
        produtobarato = produto
    total += price
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta in 'N':
        break
print('-='*15)
print(f'Total: R${total:.2f}')
print(f'{mais1000} produtos custam mais que R$1000')
print(f'O nome do produto mais barato é {produtobarato} que custa R${maisbarato:.2f}')
print('-='*15)
