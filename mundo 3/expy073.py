teams = ('Palmeiras', 'Flamengo', 'Fluminense', 'Athetico-Pr', 'Bragantino', 'Bahia', 'Coritiba', 'Sao Paulo','Atletico-MG', 'Corinthians', 'Cruzeiro', 'Botafogo','EC Vitoria', 'Internacional', 'Santos', 'Gremio', 'Vasco da Gama', 'Remo', 'Mirassol','Chapecoense')
print(f' Times no Brasileirao: {teams}')
print(f'TOP 5: {teams[0:5]} \nUltimos colocados:{teams[-4:]} \nOrdem Alfabetica: {sorted(teams)} \nPosicao Chapecoense: {teams.index('Chapecoense') + 1}')
