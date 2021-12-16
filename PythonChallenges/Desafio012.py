# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço com 5% de desconto

nome = input('Qual o nome do produto?')
valor = float(input('Qual o valor do produto? R$'))

des = valor * 0.95

print(f'O valor do(a) {nome} com 5% de desconto é:\n    R${des}')