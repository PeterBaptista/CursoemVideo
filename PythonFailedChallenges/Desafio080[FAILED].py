# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort()).
# No final, mostre a lista ordenada na tela.
from time import sleep
num = list()
for c in range(0, 5):
    num.append(int(input('Digite um número: ')))
print(num)
num2 = num[:]
for c in num:
    print(c)
    if c <= num[0] != c:
        valor = c
        num.insert(0, valor)

    elif c <= num[1] != c:
        valor = c
        num.insert(1, valor)
        num.remove(c)
    elif c <= num[2] != c:
        valor = c
        num.insert(2, valor)
        num.remove(c)
    elif c <= num[3] and num[3] != c:
        valor = c
        num.insert(3, valor)
        num.remove(c)
    sleep(2)
    print(num)


sleep(3)
print(f'Lista ordenada em ordem crescente: {num}')
