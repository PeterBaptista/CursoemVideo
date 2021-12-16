# Crie um programa onde o usuário possas digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores paraes e ímpares em ordem crescente.

temp = 0
main = [], []
for c in range(0, 7):
    temp = int(input('Digite um número: '))
    if temp % 2 == 0:
        main[0].append(temp)
    else:
        main[1].append(temp)
print(f'Par: {sorted(main[0])}')
print(f'Ímpar: {sorted(main[1])}')
