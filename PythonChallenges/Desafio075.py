# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma
# tupla. No final, mostre:

# a) Quantas vezes apareceu o valor 9;
# b) Em que posição foi digitado o primeiro valor 3;
# c) Quais foram os números pares;

num = int(input('Digite um número: ')),\
      int(input('Digite outro número: ')),\
      int(input('Digite mais um número: ')),\
      int(input('Digite o último número: '))

valor = valor3 = valor9 = valorpar = 0
for pos, c in enumerate(num):
    valor = num[pos]
    if valor == 9:
        valor9 += 1
    if valor == 3:
        valor3 = pos + 1
    if valor % 2 == 0:
        valorpar += 1

print(f'O valor 9 apareceu {valor9} vezes')
if valor3 >= 1:
    print(f'O valor 3 apareceu na {valor3}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram {valorpar}')
