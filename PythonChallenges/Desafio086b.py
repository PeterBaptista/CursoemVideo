matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
linha = coluna = 0
while linha < 3:
    for c in range(0, 3):
        num = int(input(f'Digite um número para [{linha}, {c}]: '))
        matriz[linha][c] = num
    linha += 1
linha = 0
print('Matriz 3x3')
while linha < 3:
    for d in range(0, 3):
        print(f'[{matriz[linha][d]:^5}]', end='')
    print('')
    linha += 1