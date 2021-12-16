# from time import sleep
#
# num = -1
# while True:  # While eterno
#     num += 1
#     power = 2 ** num
#     print(f'2^{num} = {power}')
#     sleep(0.1)
soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
print(f'A soma vale: {soma}')
