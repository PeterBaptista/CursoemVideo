# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

print('Bem vindo ao avaliador de triângulos!\n')
l1 = float(input('1º lado em cm: '))
l2 = float(input('2º lado em cm: '))
l3 = float(input('3º lado em cm: '))

if l1 > l2 + l3:
    print('Não é possível formar um triângulo com essas medidas.')
else:
    if l2 > l1 + l3:
        print('Não é possível formar um triângulo com essas medidas.')
    else:
        if l3 > l2 + l1:
           print('Não é possível formar um triângulo com essas medidas.')
        else:
            print('É possível formar um triângulo com essas medidas!')
