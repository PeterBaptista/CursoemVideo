# Melhore o Desafio061, perguntando para o usuário se ele quer mostrar mais
# alguns termos. O programa encerra quando ele disser que quer
# mostrar 0 termos

a1 = int(input('Digite o primeiro termo: '))
raz = int(input('Razão da P.A.: '))
termo = a1
mais = 1
cont = 1
total = 10
while mais != 0:
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer adicionar? '))
    total += mais
print(f'Progressão finalizada com {total} termos mostrados.')
