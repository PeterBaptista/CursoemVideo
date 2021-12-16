# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# Ex.: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = str(input('Qual seu nome completo? ')).strip().split()

pnome = nome[0].capitalize()
ultnome = nome[len(nome)-1]

print('processando seu nome...')

print('-'*36)
print(f'Seu primeiro nome é: {pnome}'
      f'\nSeu último nome é: {ultnome}')
print('-'*36)



