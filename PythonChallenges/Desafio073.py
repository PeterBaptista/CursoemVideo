# Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabel do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Apenas os 5 primeiros colocados.
# b) os últimos 4 colocados da tabela.
# c) uma lista com os time em ordem alfabética.
# d) em que posição na tabela está o time a Chapecoense.

times = 'Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthias',\
        'Fortaleza', 'Bragantino', 'Fluminense', 'América-MG',\
        'Atlético-GO', 'Ceará SC', 'Santos', 'Internacional',\
        'São Paulo', 'Athletico-PR', 'Cuiabá', 'Bahia',\
        'Juventude', 'Grêmio', 'Sport Recife', 'Chapecoense'

print('+='*80)
print(f'\033[32mPrimeiros 5 colocados:\033[m {times[:5]}')
print('+='*80)
print(f'\033[31mÚltimos colocados:\033[m {times[-4:]}')
print('+='*80)
print(f'\033[33mOrdem alfabética:\033[m {sorted(times)}')
print('+='*80)
print(f'A Chapecoense está na \033[31m{times.index("Chapecoense") + 1}\033[mª posição.')
