def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)


soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(2, 201)
soma(a=4, b=2)  # você pode formatar explicitando
soma(b=2, a=4)  # você pode trocar de lugar se explicitar