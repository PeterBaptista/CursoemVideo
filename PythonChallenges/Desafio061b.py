# Refaça o Desafio051, lendo primeiro termo e a razão de um P.A
# Mostrando os 10 primeiros termos progressão usando a estrutura while.

a1 = int(input('Digite o primeiro termo: '))
raz = int(input('Razão da P.A.: '))
termo = a1
cont = 1

while cont <= 10:
    print(f'{termo} → ', end='')
    termo += raz
    cont += 1
print('FIM')