# Crie um programa onde o usuário digite um expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar se a expressão
# passada está com os parênteses abertos e fechados na ordem correta.

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão está correta')
else:
    print('A expressão está incorreta')