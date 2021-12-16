# Crie um programa que leia ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

rec = ''.split()
for c in range(0, 6):
    idade = int(input('Qual é a sua idade? '))
    if idade >= 21:
        rec += str(idade).split()

if len(rec) == 1:
    print(f'{len(rec)} pessoa atingiu a maioridade.')
    print(f'{6 - len(rec)} pessoas são menores de idade')
elif len(rec) == 0:
    print(f'Nenhuma pessoa atingiu a maioridade.')
    print('6 pessoas são menores de idade')
else:
    print(f'{len(rec)} pessoas atingiram a maioridade')
    print(f'{6 - len(rec)} são menores de idade')
