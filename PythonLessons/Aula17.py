# Listas

lista = ['Hamburguer', 'Suco', 'Pizza', 'Picolé']

print(lista)

lista.append('Cookie')  # Adicionar um elemento ao final da lista
print(lista)

lista.insert(0, 'Cachorro-quente')  # Inserir um elemento na lista
print(lista)

del lista[3]  # Apagar um elemento da lista
print(lista)

lista.pop(1)  # Outra forma: Apagar um elemento da lista
print(lista)

lista.pop()   # Eliminar o último elemento
print(lista)

lista.remove('Cachorro-quente')  # Apagar um elemento indicando o valor
print(lista)

valores = list(range(4, 11))   # Cria uma lista partindo do 4 até o 10
print(valores)

valores = [8, 2, 5, 4, 9, 3, 0]   # você pode criar um lista assim
print(valores)

valores.sort()   # Colocar os valores em ordem crescente
print(valores)

valores.sort(reverse=True)   # Colocar os valores em ordem decrescente
print(valores)

print(len(valores))  # Saber quantos valores tem
