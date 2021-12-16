pessoas = {'nome': 'Pedro', 'sexo': 'M', 'idade': 19}
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-='*20)
for k in pessoas.keys():
    print(f'{k}', end=' ')
print()
for k in pessoas.values():
    print(f'{k}', end=' ')
print()
for k in pessoas.items():
    print(f'{k} ', end=' ')
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')