nl = [] # Nomes dos Produtos
prl = [] # Precos
mi = 0 # mais de 1000 reais
s = 0 # Soma do total
while True:
    n = input('Produto: ')
    p = float(input('Preco R$'))
    c = ' '
    nl.append(n)
    prl.append(p)
    if p > 1000.0:
        mi += 1
    s += p
    while c not in 'SN':
        c = input('Continuar [S/N]? ').upper()
    if c == 'N':
        break
pm = min(prl)
nm = prl.index(pm)
print('FIM')
print(f'TOTAL: R${s:.2f} \nProdutos que custam mais de 1000: {mi} \n Produto mais Barato: {nl[nm]}  R${pm}')