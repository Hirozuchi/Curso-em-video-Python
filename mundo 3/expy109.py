import coin

price = float(input('Digite o Preco: '))
print(f'Metade de {coin.coin(price)}: {coin.half(price, True)}')
print(f'Dobro de {coin.coin(price)}: {coin.double(price, True)}')
print(f'Aumentando 10% de {coin.coin(price)}: {coin.add_percent(price, 10, True)}')
print(f'Diminuindo 15% de {coin.coin(price)}: {coin.minus_percent(price, 15, True)}')