# nome = input('Qual é seu nome?')
# print('Prazer em te conhecer {:§^20}!'.format(nome))

n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
soma = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
di = n1 // n2
exp = n1 ** n2

print('A soma é {}, \n o produto é {} e a divisão é {:.3f}'.format(soma, mul, div), end=' ')
print('e a potência é {} e a divisão inteira {}'.format(exp, di))
