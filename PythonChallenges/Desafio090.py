# Faça um programa que leia nome e média de um aluno, guardando também
# a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

nome = str(input('Qual é seu nome? '))
nota1 = int(input('1ª NOTA: '))
nota2 = int(input('2ª NOTA: '))
media = (nota1 + nota2) / 2
if media < 7:
    situation = 'Reprovado'
else:
    situation = 'APROVADO'
aluno = {'nome': nome, 'média': media, 'Situação': situation}

print(f'nome: {aluno["nome"]}')
print(f'Média: {aluno["média"]}')
print(f'Situação: {aluno["Situação"]}')