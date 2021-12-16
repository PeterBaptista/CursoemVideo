# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi
# o maior e o menor valor lido. O programa deve perguntar ao usuário
# se ele quer ou não continuar a digitar valores.

num = maior = menor = soma = media = cont = 0
resposta = 'S'

while resposta not in 'N':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1
    media = soma / cont
    if num > maior or cont == 1:
        maior = num
    if num < menor or cont == 1:
        menor = num
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta != 'S' or resposta != 'N':
        while resposta not in 'SN':
            resposta = str(input('\033[31mopção inválida!\033[m [S/N]? ')).strip().upper()[0]
print(f'A média dos valores é {media:.2f}')
print(f'O maior valor é {maior}'
      f'\nO menor valor é {menor}')


