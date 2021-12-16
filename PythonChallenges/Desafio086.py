# Crie um programa que crie uma matriz de dimensão 3x3 e preencha
# com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
lista = [[], [], []]
linha = coluna = 0
while True:
    num = int(input('Digite um número: '))
    lista[linha].append(num)
    coluna += 1
    if coluna == 3:
        if linha == 2:
            break
        coluna = 0
        linha += 1
print(f'Matriz 3x3:\n{lista[0]}\n{lista[1]}\n{lista[2]}')
