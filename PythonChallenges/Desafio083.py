# Crie um programa onde o usuário digite um expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar se a expressão
# passada está com os parênteses abertos e fechados na ordem correta.
right = left = 0
n = str(input('Digite um expressão: '))

for c in range(0, len(n)):
    if n[c] == '(':
        right += 1
    elif n[c] == ')':
        left += 1

if right == left:
    print('A expressão está correta! ')
else:
    print('A expressão está incorreta!')