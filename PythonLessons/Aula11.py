# Cores no Python
# \033 [ style ;  text ; back m


print('\033[1;33mOlá, Mundo!\033[m')

a = 3.14
b = 6.10
print(f'Os valores são \033[1;32m{a}\033[m e \033[1;31m{b}\033[m')

nome = 'Pedro'
print('\nOlá! Muito prazer em te conhecer, {}{}{}'.format('\033[4;34m', nome, '\033[m'))
