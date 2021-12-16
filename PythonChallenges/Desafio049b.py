# Refaça o Desafio009, mostrando a tabuada de um número
# que o usuário escolher, ´so que agora utilizando um
# laço for.
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
