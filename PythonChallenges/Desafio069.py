# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos;
# B) Quantos homens foram cadastrados;
# C) Quantas mulheres tem menos de 20 anos;

mais18 = homem = menos20 = cont = 0
while True:
    cont += 1
    print('-='*10)
    print(f'PESSOA {cont}')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        menos20 += 1
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'Existem {mais18} pessoas maiores de 18 anos no cadastro')
print(f'{homem} homens foram cadastrados')
print(f'Existem {menos20} mulheres menores de 20 anos cadastro')
