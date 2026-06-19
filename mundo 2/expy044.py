pp = float(input('Preco produto:'))
fp = int(input('Forma de Pagamento: \n1 Dinheiro \n2 A vista cartao \n3 Parcelado no Cartao: \n'))
if fp == 1:
    vf = pp * 0.90
    print(f'Valor a pagar: R${vf:.2f}')
elif fp == 2:
    vf = pp * 0.95
    print(f'Valor a pagar: R${vf:.2f}')
elif fp == 3:
    par = int(input('Quantas vezes?'))
    if par >= 3:
        vf = pp * 1.20
        print(f'Valor a Pagar: R${vf:.2f}')
    else:
        print(f'Valor a Pagar: R${pp}')
