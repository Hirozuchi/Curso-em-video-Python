def file(name="", goals=0):
    print(f'O jogador {name} fez {goals} gol(s) no campeonato')

player = input('Nome do Jogador: ')
if not player:
    player = 'Desconhecido'
try:
    score = int(input('Numero de Gols: '))
except ValueError:
    score = 0
file(player, score)