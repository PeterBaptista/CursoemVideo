# Escreva um programa que leia um número inteiro qualquer
# e peça para usuário escolher qual será a base de conversão.

print('\033[034m-=-'*15)
print('Bem vindo ao conversor de números decimais!')
print('-=-'*15)

num = int(input('\033[mDigite um número: '))
choice = int(input('Digite 1 para converter para \033[33mBinário\033[m'
                   '\nDigite 2 para converter para \033[36mOctal\033[m'
                   '\nDigite 3 para converter para \033[31mHexadecimal\033[m\n'))

if choice > 3 and choice < 1:
    print('\033[1;031mNúmero inválido')
elif choice == 1:
    print(f'A conversão de \033[33m{num}\033[m em Binário é \033[1;33m{bin(num)[2:]}')
elif choice == 2:
    print(f'A conversão de \033[34m{num}\033[m em Octal é \033[1;34m{oct(num)[2:]} ')
elif choice == 3:
    print(f'A conversão de \033[31m{num}\033[m em Hexadecimal é \033[1;31m{hex(num)[2:]}')