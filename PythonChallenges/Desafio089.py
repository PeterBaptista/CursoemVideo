# Crie um programa que leia nome e duas notas de vários alunos e guarde
# tudo em uma lista composta, No final, mostre um boletim cintendo a média
# de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.

ficha = []

while True:
    nome = str(input('Nome: ')).capitalize()
    n1 = float(input('1ª nota: '))
    n2 = float(input('2ª nota: '))
    media = (n1 + n2) / 2
    ficha.append([nome, n1, n2, media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 24)
print(f'No. {"NOME":<15}MÉDIA')
print('-' * 24)
for pos, c in enumerate(ficha):
    print(f'{pos}   {c[0]:<15}{c[3]:.1f}')
print('-'*24)
while True:
    resp = int(input('Quer mostrar a nota de qual aluno? (999 para fechar): '))
    if resp == 999:
        break
    print(f'Notas de {ficha[resp][0]} são {ficha[resp][1]} e {ficha[resp][2]}')
    print('-'*24)
