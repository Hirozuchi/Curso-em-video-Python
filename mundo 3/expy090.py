data = {}
data['name'] = input('Nome: ')
data['average'] = float(input('Media: '))
if data['average'] >= 6:
    data['pass'] = 'Aprovado'
else:
    data['pass'] = 'Reprovado'
print(f'Nome: {data["name"]} \nMedia: {data["average"]} \nSituacao: {data["pass"]}')
