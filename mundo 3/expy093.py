data = {}
data['name'] = input('Nome do Jogador: ')
matches = int(input(f'Quantas partidas {data["name"]} jogou? '))
goals = []
n = 0
for goal in range(0, matches):
    g_match = int(input(f'Quantos gols na partida {goal + 1}: '))
    goals.append(g_match)
data['goals'] = goals
data['total'] = sum(goals)
for k, v in data.items():
    print(f'{k}: {v}')
print('>+_+<' * 20)
print(f' O jogador {data["name"]} jogou {matches} partidas')
for g in goals:
    n += 1
    print(f'Na partida {n}, fez {g} gols')
print(f'Total de gols foi {data["total"]}')