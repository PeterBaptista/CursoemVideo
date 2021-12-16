# Crie um programa que leia nome, sexo e idade de várioas pessoas, guardando
# os dados de cada pessoa em um dicionário e todos os dicionários em uma
# lista. No final, mostre:
# A) Quantas pessoas cadastradas;
# B) A média de idade;
# C) Uma lista com mulheres;
# D) Uma lista com idade acima da média;
pessoa = {}
fichas = list()
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('Erro! Você deve digitar M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    fichas.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? ')).upper().strip()[0]
        if resp in 'SN':
            break
        else:
            print('Erro! A resposta deve ser S ou N.')
    if resp in 'N':
        break
print('-='*20)
print(f'{len(fichas)} pessoas foram cadastradas.')
soma = media = 0
mulheres = list()
acimamedia = list()
for pos, v in enumerate(fichas):
    soma += fichas[pos]['idade']
    if fichas[pos]['sexo'] in 'F':
        mulheres.append(fichas[pos]['nome'])
media = soma / len(fichas)
print(f'A média de idade é igual a \033[36m{media:.1f} anos\033[m')
print(f'Nome das mulheres cadastradas:\033[36m{mulheres}\033[m ')
print('Lista de pessoas acima da média de idade:')
for pos, v in enumerate(fichas):
    if fichas[pos]['idade'] > media:
        for k, v in fichas[pos].items():
            print(f'\033[34m{k}:\033[m{v}; ', end='')
        print()
print('      \033[31m<<ENCERRADO>>\033[m')
 