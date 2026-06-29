import tabulate
data = {}
goals = []
people = []
while True:
    data['name'] = input('Nome do Jogador: ')
    matches = int(input(f'Quantas partidas {data["name"]} jogou? '))
    for goal in range(0, matches):
        g_match = int(input(f'Quantos gols na partida {goal + 1}: '))
        goals.append(g_match)
    data['goals'] = goals[:]
    data['total'] = sum(goals)
    people.append(data.copy())
    goals.clear()
    yesorno = ' '
    while yesorno not in 'SN':
        yesorno = input('Continuar [S/N]? ').upper()
    if yesorno == 'N':
        break
header = {'name': 'Nome', 'goals': 'Gols', 'total': 'Total'}
print(tabulate.tabulate(people, headers=header, tablefmt='grid', showindex=True))
while True:
    player_data = int(input('Visualizar Dados de qual Jogador? '))
    if player_data == 999:
        break
    if player_data >= 0 and player_data < len(people):
        print(f'Levantamento do jogador {people[player_data]["name"]}:')
        for i, g in enumerate(people[player_data]["goals"], start=1):
            print(f'No jogo {i} fez {g} gols')
    else:
        print('Nao possui um Jogador salvo nessa posicao, Tente Novamente')
