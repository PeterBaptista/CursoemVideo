# Desenvolva um lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com
# a tabela abaixo:

# -Abaixo de 18.5: Abaixo do Peso
# -Entre 18.5 e 25: Peso ideal
# -25 até 30: Sobrepeso
# -30 até 40: Obesidade
# -Acima de 40: Obesidade mórbida

altura = float(input('Qual é sua altura em metros? '))
peso = float(input('Qual é seu peso em Kg? '))

imc = float(peso / (altura**2))

if imc < 18.5:
    print('\033[31mAbaixo do peso')
elif 18.5 <= imc < 25:
    print('\033[32mPeso ideal')
elif 25 <= imc < 30:
    print('\033[33mSobrepeso')
elif 30 <= imc < 40:
    print('\033[36mObesidade')
else:
    print('\033[31mObesidade Mórbida')

print(f'Resultado: {imc:.1f}')
