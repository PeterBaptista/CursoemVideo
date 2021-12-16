# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.

# Para salários superiores a R$1.250,00, calcule um aumento de 10%.

# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual o valor do seu salário? R$'))

if sal > 1250:
    print(f'O seu salário com aumento é R${sal * 1.1:.2f}')
else:
    print(f'O seu salário com aumento é R${sal*1.15:.2f}')


