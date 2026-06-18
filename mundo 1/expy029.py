vcr = float(input('Qual a velocidade do seu carro?'))
m = 7
if vcr > 80:
    m = 7 * (vcr - 80)
    print(f'Você está dirigindo acima do limite! Sua multa é {m:.2f} reais')
else:
    print('Você está dirigindo com segurança tenha uma boa viagem!')