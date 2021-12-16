pessoas = {'nome': 'Pedro', 'sexo': 'M', 'idade': 19}
del pessoas['sexo']
pessoas['nome'] = 'Allysson'  # Troquei o nome
pessoas['idade'] = 20  # Troquei a idade
pessoas['peso'] = 65.3  # adicionei o peso ao dicionário
for k, v in pessoas.items():
    print(f'{k} = {v}')