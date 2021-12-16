# Faça um programa que leia 5 valores e guarde-os em uma lista.

# No final, mostre qual foi o maior e o menor valor digitado e
# suas reapectivas posições na lista.

num = list()
for c in range(0, 5):
    num.append(int(input('Type a number: ')))

maior = menor = 0
posmaior = list()
posmenor = list()
for pos, valor in enumerate(num):
    if pos == 0:
        maior = num[pos]
        menor = num[pos]
    if num[pos] >= maior:
        if num[pos] == maior:
            posmaior.append(pos)
        else:
            del posmaior[:]
            posmaior.append(pos)
        maior = num[pos]

    if num[pos] <= menor:
        if num[pos] == menor:
            posmenor.append(pos)
        else:
            del posmenor[:]
            posmenor.append(pos)
        menor = num[pos]

print(f'O maior número é {maior} e está nas posições', end=' ')
for c in posmaior:
    print(f'...{c}', end='')
print(f'\nO menor número é {menor} e está na posições', end=' ')
for c in posmenor:
    print(f'...{c}', end='')
