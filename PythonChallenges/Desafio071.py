# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No ínicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.

# OBS.: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
print('='*30)
print('        Banco do Pedro')
print('='*30)
valor = int(input('Qual o valor que deseja sacar? R$'))
rs50 = valor // 50
rs20 = (valor - 50*rs50) // 20
rs10 = (valor - 50*rs50 - 20*rs20) // 10
rs1 = (valor - 50*rs50 - 20*rs20 - 10*rs10)

print(f'R$50 x {rs50}'
      f'\nR$20 x {rs20}'
      f'\nR$10 x {rs10}'
      f'\nR$1 x {rs1}')
print('Volte Sempre!')