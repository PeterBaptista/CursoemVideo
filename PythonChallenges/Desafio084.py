# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# a) Quantas pessoas foram cadastradas;
# b) Uma listagem com as pessoas mais pesadas;
# c) Uma listagem com as pessoas mais leves;

maispesada = list()
maisleve = list()
cont = 0
while True:
    print(f'PESSOA [{cont + 1}]')
    pessoa = input('Nome: ')
    peso = float(input('Peso em Kg: '))
    if peso >= 90:
        maispesada.append([pessoa, peso])
    else:
        maisleve.append([pessoa, peso])

    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
    print('--'*20)
print(f'Foram cadastradas {cont} pessoas')
print('\nPessoas mais leves: ')
for pos, c in enumerate(maisleve):
    print(f'{maisleve[pos][0]} → {maisleve[pos][1]}Kg')
print('\nPessoas mais pesadas: ')
for pos, c in enumerate(maispesada):
    print(f'{maispesada[pos][0]} → {maispesada[pos][1]}Kg')



