# Refaça o Desafio051, lendo primeiro termo e a razão de um P.A
# Mostrando os 10 primeiros termos progressão usando a estrutura while.

a1 = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
num = 0
resul = 0
mult = ''
while num != 10:
    result = a1 + num * raz
    num += 1
    if num != 10:
        mult += f'{result} → '
    else:
        mult += f'{result}'

print(f'{mult}')
