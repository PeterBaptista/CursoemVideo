# Faça um programa que mostre na tela uma contagem regressiva para o estouto
# de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
import emoji
fw = emoji.emojize(':boom:', use_aliases= True)

print('Bem-vindo ao lançador de fogos de artifício!')


n = int(input('Digite [1] para detonar: '))

if n == 1:
    for c in range(10, -1, -1):
        print(c)
        sleep(1)

print(f'\033[31m{fw}BOOOOOM!')
sleep(0.8)
print('Fogos de artíficio lançados com sucesso.')



