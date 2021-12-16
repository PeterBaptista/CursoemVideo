# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogadas = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
ranking = list()
print('VALORES SORTEADOS...')
for k, v in jogadas.items():
    print(f'\033[31m{k}\033[m tirou {v}')
    sleep(0.75)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('  ========= RANKING =========')
for pos, c in enumerate(ranking):
    print(f'   {pos+1}º lugar → \033[34m{c[0]}\033[m com {c[1]}')
    sleep(1)