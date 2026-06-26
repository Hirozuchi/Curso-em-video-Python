info = []
data = []
count = 0
while True:
    data.append(str(input('Nome: ')))
    data.append(float(input('Peso: ')))
    info.append(data[:])
    data.clear()
    count += 1
    yes_no = ' '
    while yes_no not in 'SN':
        yes_no = input('Quer continuar [S/N] ').upper()
    if yes_no == 'N':
        break
max_weight = max(weight[1] for weight in info)
min_weight = min(weight[1] for weight in info)
max_name = []
min_name = []
for weight in info:
    if weight[1] == max_weight:
        max_name.append(weight[0])
    if weight[1] == min_weight:
        min_name.append(weight[0])
print(f'Pessoas Cadastradas: {count}')
print(f'Maior Peso: {max_weight}KG, Peso de ', end='')
for name in max_name:
    print(f'{name}', end=' ')
print(f'\nMenor Peso: {min_weight}KG, Peso de ', end='')
for name in min_name:
    print(f'{name}', end=' ')