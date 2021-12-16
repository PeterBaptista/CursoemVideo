# Crie um programa que tenha uma tupla única com nomes
# de produtos e seus respectivos preços na sequência.
# No final, mostre um listagem de preços, organizando os dados em forma tabular.

itens = 'Arroz', 6.10, 'Leite', 4.20,\
        '12 ovos', 8.70, 'Feijão', 9.50,\
        'Maçã', 4.99, 'Oreo', 3.30, \
        'Whiskey', 46.73, 'Coca-Cola 600ml', 4.09, \
        'Wagyu 500g', 599.34
print('-'*38)
print('\033[7;1;4;33;40m{:^38}\033[m'.format('Tabela de Preços'))
print('-'*38)
produto = itens[::2]
preco = itens[1::2]
cont = 0
while cont < len(produto):
    produto1 = produto[cont]
    preco1 = preco[cont]
    print(f'{produto1:.<30}R${preco1:>6.2f}')
    cont += 1
print('-'*38)


