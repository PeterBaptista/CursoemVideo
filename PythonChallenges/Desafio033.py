# Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

if n1 > n2 > n3:
    print(f'O número {n1} é maior e {n3} o menor')
else:
    if n1 > n3 > n2:
        print(f'O número {n2} é o maior e {n3} o menor')
    else:
        if n2 > n1 > n3:
            print(f'O número {n2} é o maior e {n3} o menor')
        else:
            if n2 > n3 > n1:
                print(f'O número {n2} é o maior e {n1} o menor')
            else:
                if n3 > n2 > n1:
                    print(f'O número {n3} é o maior e {n1} o menor')
                else:
                    if n3 > n1 > n2:
                        print(f'O número {n3} é o maior e {n2} o menor')

