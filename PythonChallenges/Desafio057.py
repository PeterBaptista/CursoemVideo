# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M'
# ou 'F'. Caso esteja errado peça esteja errado, peça a digitação novamente
# até ter um valor correto.

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while sexo not in 'MF':
     sexo = str(input('\033[31mRESPOSTA INVÁLIDA, DIGITE NOVAMENTE: [M/F]\033[m ')).strip().upper()[0]

if sexo == 'M':
    print('\033[34m[Sexo masculino]\033[m, Dado recebido com sucesso!')
else:
    print('\033[1;31m[Sexo Feminino]\033[m, Dado recebido com sucesso!')

