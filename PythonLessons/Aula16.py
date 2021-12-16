# Tuplas
# Tuplas são imutáveis!
# lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Tapioca'
# print(len(lanche),'itens')
# for comida in lanche:
#     print(f'Eu vou comer {comida};')
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos + 1}')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(c)
print(c.index(5, 2))