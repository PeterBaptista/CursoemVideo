# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados;
# b) A soma dos vaçores da terceira coluna;
# c) O maior valor da segunda linha;
par = l2maior = coluna3 = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l][c] = num
        if num % 2 == 0:
            par += num
        if c == 2:
            coluna3 += num
        if l == 1 and c == 0:
           l2maior = matriz[1][0]
        elif l == 1:
            if l2maior < matriz[l][c]:
                l2maior = matriz[l][c]
print('-='*11)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*11)
print(f'A soma dos valores pares digitados é {par}')
print(f'A soma dos valores da terceira coluna é {coluna3}')
print(f'O maior valor da segunda linha é {l2maior}')
