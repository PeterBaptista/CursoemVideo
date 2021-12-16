# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai para quando o usuário digitar o valor 999, que é a
# condição de parada. No final, mostre quantos números foram digitados e qual
#  foi a soma entre eles (desconsiderando o flag)

num = 0
soma = 0
quant = ''
print('Para terminar digite [999]')
while num != 999:
    num = int(input('Digite um número inteiro: '))
    if num != 999:
        quant += str(num)
        soma += num
print('~'*34)
print(f'A soma do valores é igual a {soma}'
      f'\nVocê digitou {len(quant)} números')
print('~'*34)
