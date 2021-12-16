# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.7
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()
cont = 0

while True:
    cont += 1
    n = int(input('Digite um valor: '))
    lista.append(n)
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resposta in 'SN':
            break
    if resposta in 'N':
        break

print(f'lista: {lista}')
print(f'Foram digitados {cont} números')
lista.sort(reverse=True)
print(f'Ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista')
