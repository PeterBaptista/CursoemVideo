# Faça um programa que tenha uma função chamada escreva(), que receba um texto
# qualquer como parâmetrp e mostre uma mensagem com tamanho adaptável.

# Ex.:
# escreva('Olá, mundo!')
# Saída:
# ------------
# Olá, mundo!
# ------------

def formatador(msg):
    print('-'*(len(msg)+4))
    print(f'  {msg:}')
    print('-'*(len(msg)+4))

formatador('Pedro')
formatador('MUITO BOM!')
