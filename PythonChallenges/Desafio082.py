# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente. Ao final, mostre
# o conteúdo das três listas geradas.

num = list()
numpar = list()
numimpar = list()
while True:
    n = int(input('Digite um número: '))
    num.append(n)
    if n % 2 == 0:
        numpar.append(n)
    else:
        numimpar.append(n)
    while True:
        resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if resposta in 'SN':
            break
    if resposta in 'N':
        break
print(f'A lista completa: {num}')
print(f'números pares: {numpar}')
print(f'números ímpares: {numimpar}')