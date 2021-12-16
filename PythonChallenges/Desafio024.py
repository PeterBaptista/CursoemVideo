# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Digite o nome de uma cidade: ')).strip()


upper = cidade.upper()
split = upper.split()
n1 = split[0]
tem = 'SANTO' in n1

print('A cidade começa com o nome SANTO?', tem)
