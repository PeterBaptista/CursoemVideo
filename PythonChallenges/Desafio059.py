# Crie um programa que leia dois valores e mostre um menu na tela:
# - [1] somar
# - [2] multiplicar
# - [3] maior
# - [4] novos números
# - [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
num1 = float(input('1º valor: '))
num2 = float(input('2º valor: '))
escolha = 0
while escolha != 5:
    print('[1]Somar'
          '\n[2]Multiplicar'
          '\n[3]Maior'
          '\n[4]Novos números'
          '\n[5]Sair do programa')
    escolha = int(input('>>>>> Qual é a sua opção?  '))
    if escolha == 1:
        print(num1 + num2)
    elif escolha == 2:
        print(num1 * num2)
    elif escolha == 3:
        if num1 < num2:
            print(f'\033[33mO número {num2} é maior\033[m')
        elif num1 > num2:
            print(f'\033[33mO número {num1} é maior\033[m')

    elif escolha == 4:
        num1 = float(input('1º valor: '))
        num2 = float(input('2º valor: '))
    else:
        print('\033[31mOpcão inválida, tente novamente!\033[m')
    print('-='*10)
    sleep(1.5)

print('Obrigado por usar meu programa! ')

