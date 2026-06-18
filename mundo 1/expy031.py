dis = float(input('Qual a distancia da sua viagem?'))
if dis <=200:
   v = dis * 0.50
   print(f'O valor da sua passagem e {v:.2f} reais')
elif dis > 200:
   v = dis * 0.45
   print(f'O valor da sua passagem e {v:.2f} reais')