# Crie um programa que tenha um tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = 'Adeus', 'Sofia', 'Pedro', 'Paralelepido',\
           'Deus', 'Allysson', 'Roblox', 'Dinheiro'
cont = cont2 = 0

while cont < len(palavras):
    vogais = ''
    cont2 = 0
    word = palavras[cont].lower().strip()
    while cont2 < len(word):
        if word[cont2] in 'aeiou':
            vogais += '\033[1;34m{}\033[m '.format(word[cont2])
        cont2 += 1
    print(f'Na palavra \033[1;4;35m{word.upper()}\033[m temos as vogais: {vogais}')
    cont += 1