namel = [] # Nomes dos Produtos
pricel = [] # Precos
mil = 0 # mais de 1000 reais
add = 0 # Soma do total
while True:
    name = input('Produto: ')
    price = float(input('Preco R$'))
    yesorno = ' '
    namel.append(name)
    pricel.append(price)
    if price > 1000.0:
        mi += 1
    add += price
    while yesorno not in 'SN':
        yesorno = input('Continuar [S/N]? ').upper()
    if yesorno == 'N':
        break
pricemin = min(pricel)
namepos = pricel.index(pricemin)
print('FIM')
print(f'TOTAL: R${add:.2f} \nProdutos que custam mais de 1000: {mi} \n Produto mais Barato: {namel[namepos]}  R${pricemin}')