# Faça um program que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessaria para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²

H = float(input('Qual a altura da sua parede? '))
L = float(input('Qual a largura da sua parede? '))

ar = H * L
li = ar / 2

print(f'\nÁrea = {ar}m²\n Litros de tinta = {li}l')