# Crie um programa que leia onome completo de uma pesooa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = input('Qual é o seu nome completo?')

strip = nome.strip()
stsp = strip.split()
junto = ''.join(stsp)

print('Maiúsculas: ', nome.upper())
print('Minúsculas: ', nome.lower())
print('Seu nome completo tem: ', len(junto), 'letras')
print('Seu primeiro nome tem: ', len(nome.split()[0]), 'letras')

