# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.


print('Bem vindo ao analisador de anos BISSEXTOS')
# obs.: ao invés de colocar ".format( )" eu coloquei "f" no começo do print( ).

ano = int(input('Digite um ano qualquer: '))

if ano == 0:
    print('O ano 2021 não é Bissexto')
elif ano % 400 == 0 and ano % 100 == 0:
    print(f'O ano {ano} é Bissexto')
elif ano % 400 != 0 and ano % 100 == 0:
    print(f'O ano {ano} não é Bissexto')
elif ano % 4 == 0:
    print(f'O ano {ano} é Bissexto')
else:
    print(f'O ano {ano} não é Bissexto')
