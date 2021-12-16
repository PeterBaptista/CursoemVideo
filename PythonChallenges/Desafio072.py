# Crie um programa que tenha uma tupla totalmente preenchida
# com um contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado(entre 0 e 20)
# e mostrá-lo por extenso.

extenso = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', \
          'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', \
          'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',\
          'Dezenove', 'Vinte'
n = -1
while True:
    while n < 0 or n > 20:
        n = int(input('Digite um número entre 0 e 20: '))
    print(extenso[n])
    n = -1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break

