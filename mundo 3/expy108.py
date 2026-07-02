import coin

price = float(input('Digite o Preco: '))
print(f'Metade de {coin.coin(price)}: {coin.coin(coin.half(price))}')
print(f'Dobro de {coin.coin(price)}: {coin.coin(coin.double(price))}')
print(f'Aumentando 10% de {coin.coin(price)}: {coin.coin(coin.add_percent(price, 10))}')
print(f'Diminuindo 15% de {coin.coin(price)}: {coin.coin(coin.minus_percent(price, 15))}')