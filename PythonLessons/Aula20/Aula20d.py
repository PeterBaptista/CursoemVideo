def contador(*num):  # "*" + "num" cria um tupla com os valores digitados
    for valor in num:
        print(f'{valor} ', end='')
    print('Fim!')


contador(2, 3, 1, 0)
contador(10, 2, 4, 3)