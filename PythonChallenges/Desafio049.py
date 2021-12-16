# Refaça o Desafio009, mostrando a tabuada de um número
# que o usuário escolher, ´so que agora utilizando um
# laço for
num = int(input('Digite um número: '))
print(f'Tabuada de {num}:')
for c in range(1, 11):
    print(f'{num} x {c} = {num*c}')