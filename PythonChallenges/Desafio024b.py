# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO"

cid = str(input('Qual o nome da cidade?')).strip()

print('O nome da cidade começa com SANTO? {}'.format(cid.upper()[:5] == 'SANTO'))

