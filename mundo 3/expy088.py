import random
from time import sleep
plays_list = []
guesses = []
games = int(input('Quantos jogos?: '))
for plays in range(0, games):
    guess = sorted(random.sample(range(1, 61), 6))
    plays_list.append(guess)
    print(f'Jogo {plays + 1}: {plays_list[plays]}')
    sleep(1)