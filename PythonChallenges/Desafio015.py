# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias  pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia
# e R$0,15 por KM rodado.

kmpe = float(input('Quantos Km o seu carro percorreu?'))
qdia = int(input('Por quantos dias o carro foi alugado?'))

pre = qdia * 60 + kmpe * 0.15

print(f'Você deverá pagar R${pre:.2f}')
