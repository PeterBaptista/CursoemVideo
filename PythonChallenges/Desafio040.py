# Crie um programa que leia duas notas de um aluno e calcule sua
# média, mostrando uma mensagem no final, de acordo com
# a média atingida:

# -Média abaixo de 5.0: Reprovado
# -Média entre 5.0 e 6.9: Recuperação
# -Média 7.0 ou superior: Aprovado

print('-=-'*12)
print('\033[033mDescubra sua situação na escola!\033[m')
print('--='*12)

n1 = float(input('\nNota da 1ª unidade: '))
n2 = float(input('Nota da 2ª unidade: '))
n3 = float(input('Nota da 3ª unidade: '))
n4 = float(input('Nota da 4ª unidade: '))

med = (n1 + n2 + n3 + n4)/4

if med < 5:
    print('\033[031mREPROVADO')
elif 5 <= med <= 5.9:
    print('\033[034mRECUPERAÇÃO')
else:
    print('\033[1;032mAPROVADO')

