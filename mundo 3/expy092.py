from datetime import datetime
data = {}
data['name'] = input('Nome:')
birth_year = int(input('Ano de Nascimento:'))
data['age'] = datetime.now().year - birth_year
data['ctps'] = int(input('Possui Carteira de trabalho [0 NAO]? '))
if data['ctps'] != 0:
    data['contract_year'] = int(input('Ano de Contratacao: '))
    data['salary'] = int(input('Salario: '))
    data['retirement'] = data['age'] + (data['contract_year'] + 35) - datetime.now().year
    for k, v in data.items():
        print(f' {k}:{v}')
else:
    for k, v in data.items():
        print(f'{k}: {v}')