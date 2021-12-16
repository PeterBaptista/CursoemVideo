# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

num = list()
cont = 0
while True:
    num.append(int(input('Type a value: ')))
    if num[cont] in num[:cont]:
        num.remove(num[cont])
        cont -= 1

    cont += 1
    if 999 in num:
        num.remove(999)
        break
print('O valores, sem repetição, em ordem crescente, que foram digitados são:\n', sorted(num))