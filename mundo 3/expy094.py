data = {}
fem = []
above_average = []
people = []
total = 0
while True:
    name = input('Nome: ')
    data['name'] = name
    sex = ' '
    while sex not in 'MF':
        sex = input('Sexo [M/F]:').upper()
    data['sex'] = sex
    if sex == 'F':
        fem.append(name)
    age = int(input('Idade: '))
    data['age'] = age
    people.append(data.copy())
    total += 1
    yesorno = ' '
    while yesorno not in 'SN':
        yesorno = input('Continuar [S/N]? ').upper()
    if yesorno == 'N':
        break
average = sum(p['age'] for p in people) / total
for p in people:
    if p['age'] > average:
        above_average.append(p)
print(f'Pessoas cadastradas: {total} \nMedia: {average} anos \nMulheres: {fem} \nAcima da Media: {above_average}')