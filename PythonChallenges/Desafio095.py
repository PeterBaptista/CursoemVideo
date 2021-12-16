# Aprimore o DESAFIO093 para que ele funcione com vários jogadores, incluindo um
# sistema de visualização de detalhes do aproveitamento de cada jogador.
ficha = {}
gols = []
time = []
while True:
    ficha['nome'] = str(input('Nome do jogador: '))
    ficha['partidas'] = int(input('Quantas partidas jogou? '))
    for c in range(0, ficha['partidas']):
        gols.append(int(input(f'Quantos gols marcou na {c+1}ª partida? ')))
    total = sum(gols)
    ficha['gols'] = gols[:]
    ficha['total'] = total
    time.append(ficha.copy())  # Lista de todos os jogadores
    gols.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        else:
            print('Erro! Você deve digitar S ou N.')
    if resp in 'N':
        break
print(time)
print('-='*30)
print(f'{"cod":<4}{"nome":<12}{"gols":<30}{"total":<6}')
print('--'*30)
for pos, c in enumerate(time):
    print(f'{pos:<4}'
          f'{time[pos]["nome"]:<15}'
          f'{str(time[pos]["gols"]):<30}'
          f'{str(time[pos]["total"]):<6}')
while True:
    print('--'*39)
    busca = int(input('Digite o cod do jogador que você que buscar! (999 para fechar) '))
    if busca == 999:
        break
    if 0 <= busca < len(time):
        print(f'-- Levantamento do jogador \"{time[busca]["nome"]}\" --')
        for pos, v in enumerate(time[busca]['gols']):
            print(f'   No jogo {pos+1} fez {v}')
    else:
        print('Erro! digite um cod válido!')
print('Programa Finalizado com sucesso!')