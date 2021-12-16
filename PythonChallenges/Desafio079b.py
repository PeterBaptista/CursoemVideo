# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

num = list()
cont = 0

while True:
    num.append(int(input('Digite um número: ')))
    if num[cont] in num[:cont]:
        num.remove(num[cont])
        cont -= 1
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso!')
    while True:
        resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if resposta in 'SN':
            break
    if resposta in 'N':
        break
    cont += 1

print(f'Os valores adicionados em ordem crescente:\n{sorted(num)}')


