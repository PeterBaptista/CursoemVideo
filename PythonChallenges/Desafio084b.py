main = []
temp = []
maior = menor = cont = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    main.append(temp[:])
    temp.clear()
    cont += 1

    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
for pos, c in enumerate(main):
    if pos == 0:
        maior = main[0][1]
        menor = main[0][1]
    if main[pos][1] >= maior:
        maior = main[pos][1]
    if main[pos][1] <= menor:
        menor = main[pos][1]
print(f'Ao todo você cadastrou {cont} pessoas')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for pos, c in enumerate(main):
    if maior == main[pos][1]:
        print(f'{main[pos][0]}', end=' ')
print(f'\nO menor peso foi {menor}Kg. Peso de ', end='')
for pos, c in enumerate(main):
    if menor == main[pos][1]:
        print(f'{main[pos][0]}', end=' ')
