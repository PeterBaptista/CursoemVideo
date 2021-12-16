# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

# -À vista dinheiro/cheque: 10% de desconto
# -À vista no cartão: 5% de desconto
# -Em até 2x no cartão: preço normal
# -3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' Lojas Baptista '))
valor = float(input('Qual o valor a ser pago?\nR$'))

forma = int(input('[1] À vista dinheiro ou cheque: 10% de desconto'
                  '\n[2] À vista no cartão: 5% de desconto'
                  '\n[3] 2x vezes no cartão: preço normal'
                  '\n[4] 3x ou mais no cartão: 20% de juros'
                  '\n\n\033[33mQual a forma de pagamento? \033[m '))

if forma == 1:
    print('O valor total é: R${:.2f}'.format(valor * 0.9))
elif forma == 2:
    print('O valor total é: R${:.2f}'.format(valor * 0.95))
elif forma == 3:
    print(f'O valor é: R${valor / 2:.2f} em 2x')
elif forma == 4:
    meses = int(input('Quantos meses? '))
    print(f'O valor é: R${(valor / meses) * 1.2:.2f} em {meses}x')
