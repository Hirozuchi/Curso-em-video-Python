from random import randint
from time import sleep
plays = {}
n = 0
for player in range(0, 4):
    dice = randint(1, 6)
    print(f'o Jogador {player + 1}, jogou {dice}')
    plays[f' Player_{player + 1}'] = dice
    sleep(0.5)
print('Ranking dos Jogadores:')
sleep(0.5)
for k, v in sorted(plays.items(), key= lambda item: item[1], reverse= True):
    n += 1
    print(f'{n} lugar: {k} com {v}')
    sleep(0.5)