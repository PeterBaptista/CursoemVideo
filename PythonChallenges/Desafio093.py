# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler
# a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em
# um dicionário, incluindo o total de gols feitos durante o campeonato.

ficha = dict()
ficha['nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas o {ficha["nome"]} jogou? '))
ficha['gols'] = []
total = 0
for c in range(0, partidas):
    ficha['gols'].append(int(input(f'Quantos gols na {c+1}ª partida? ')))
    total += ficha['gols'][c]
ficha['total'] = total
print('-='*30)
print(ficha)
print('-='*30)
for k, v in ficha.items():
    print(f'{k}: {v}')
print('-='*30)
print(f'O jogador \033[31m{ficha["nome"]}\033[m jogou {partidas} partidas!')
for pos, v in enumerate(ficha['gols']):
    print(f'---> Na partida {pos+1}, fez {ficha["gols"][pos]} gols;')
print(f'Foi um total de \033[34m{total}\033[m gols!')
