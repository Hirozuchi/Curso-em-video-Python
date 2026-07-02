import coin

price = float(input('Digite o Preco: '))
print(f'Metade de {price}: {coin.half(price)}')
print(f'Dobro de {price}: {coin.double(price)}')
print(f'Aumentando 10% de {price}: {coin.add_percent(price, 10)}')
print(f'Diminuindo 15% de {price}: {coin.minus_percent(price, 15)}')