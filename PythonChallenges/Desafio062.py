# Melhore o Desafio061, perguntando para o usuário se ele quer mostrar mais
# alguns termos. O programa encerra quando ele disser que quer
# mostrar 0 termos

a1 = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
termo = a1
cont = 1
resposta = 1
quant = 10
while resposta != 0:
    print(f'{termo} → ', end='')
    termo += raz
    cont += 1
    if cont == 11:
        print('...')
        resposta = int(input('Quantos termos você quer adicionar? '))
        quant += resposta
        cont -= resposta

print(f'Progressão finalizada com {quant} termos mostrados.')
