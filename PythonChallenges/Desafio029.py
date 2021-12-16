# Escreva um programa que leia a velocidade de um carro.

# Se ele ultrapassar 80Km/h, mostre uma mensagem duzendo que ele foi multado.
# obs.: A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Qual foi a velocidade do carro? '))

if vel <= 80:
    print('O seu carro estava dentro dos limites de velocidade.')
else:
    print('Você foi multado! O limite de velocidade era 80Km/h'
          '\n  Calculando sua dívida...')
    print(f'O valor da multa é R${float((vel-80)*7):.2f}')
    print(f'\nVocê deverá pagá-la até 31/12/2021')