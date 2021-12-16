# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:

# - A média de idade do grupo;
# - Qual é o nome do homem mais velho;
# - Quantas mulheres têm menos de 20 anos.
people = int(input('Quantidade de pessoas: '))
listnome = []
listidade = []
listsexo = []
listpessoa = []
for c in range(1, people + 1):
    print('========= {}ªpessoa ========='.format(c))
    nome = str(input('Qual é o seu nome? ')).split()
    idade = str(input('Qual é a sua idade? ')).split()
    sexo = str(input('Sexo masculino[1], feminino[2]: ')).split()
    listnome += nome
    listidade += idade
    listsexo += sexo

med = 0
average = 0
for age in range(0, people):
    idade2 = int(listidade[age])
    med += idade2
    average = int(med/len(listidade))

maisvelho = 0
nomemaisvelho = ''
for older in range(0, people):
    gender = int(listsexo[older])
    idade2 = int(listidade[older])
    if idade2 > maisvelho and gender == 1:
        maisvelho = idade2
        nomemaisvelho = listnome[older]

menor20 = 0
for woman in range(1, people):
    gender = int(listsexo[woman])
    idade2 = int(listidade[woman])
    if gender == 2 and idade2 < 20:
        menor20 += 1

print(f'A média de idade do grupo é {average} anos')
if maisvelho == 0:
    print('Não há homens')
else:
    print(f'O homem mais velho é {nomemaisvelho}')

if menor20 == 1:
    print(f'Existe uma mulher menor de 20 anos ')
elif menor20 > 1:
    print(f'Existem {menor20} mulheres menores de 20 anos')
else:
    print('Não há mulheres menores que 20 anos no grupo')
