# A confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:

# - Até 9 anos: MIRIM
# - Até 14 anos: Infantil
# - Até 19 anos: Junior
# - Até 25 anos: Sênior
# - Acima: Master

from datetime import date

atual = date.today().year
nas = int(input('Ano de Nascimento: '))
idade = atual - nas

print('O atleta tem {} anos, sua categoria é '.format(idade), end='')
if idade <= 9:
    print('\033[036mMIRIM\033[m')
elif idade <= 14:
    print('\033[034mINFANTIL\033[m')
elif idade <= 19:
    print('\033[33mJUNIOR\033[m')
elif idade <= 25:
    print('\033[35mSÊNIOR\033[m')
else:
    print('\033[1;31mMASTER')
