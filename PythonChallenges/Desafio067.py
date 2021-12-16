# Faça um programa que mostre a tabuada de vários números, um de cada vez, para
# cada valor digitado pelo usuário. O programa será interrompiido quando o número
# solicitado for negativo.
cont = 0
while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    print('-'*34)
    print(f'\033[35mTabuada de {valor}\033[m')
    for c in range(1, 11):
        print(f'{valor} x {c:2} = {valor*c}')
    print('-'*34)
print('PROGRAMA FINALIZADO')