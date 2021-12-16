# Faça um programa que leia uma frase pelo teclado e mostres:
# 1.Quantas vezes aparece a letra "A".
# 2.Em que posição ela aparece a primeira vez.
# 3.Em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').upper().strip()

frase2 = frase.replace('À', 'A').replace('Á', 'A').replace('Ã', 'A').replace('Â', 'A')

numA = frase2.count('A')
aprim = frase2.find('A') + 1
ault = frase2.rfind('A') + 1

print(f'A letra [a] aparece: {numA} vezes')
print(f'A letra [a] apareceu primeiro na posição: {aprim}')
print(f'A letra [a] apareceu por último na posição: {ault}')


