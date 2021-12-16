# Refaça o Desafio035 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:

# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l2 + l1:
    print('\033[1;31mNão é possível formar um triângulo com essas medidas!\033[m')
elif (l1 == l2 and l1 != l3) or (l1 == l3 and l2 != l1) or (l2 == l3 and l2 != l1):
    print('\033[1;32mTriângulo Isósceles')
elif l1 == l2 == l3:
    print('\033[1;32mTriângulo Equilátero')
elif l1 != l2 != l3 != l1:
    print('\033[1;32mTriângulo Escaleno')