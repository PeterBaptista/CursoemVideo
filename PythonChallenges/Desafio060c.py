# Fazer o Desafio060 usando while e for.

n = int(input('Digite um valor para calcular o fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ')
for fat in range(1, n):
    if fat > 1:
        print(f'{fat} x ')
    else:
        print(f'{fat} = ')
    f *= fat
print(f)