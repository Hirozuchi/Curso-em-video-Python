productname = float(input('Preco produto:'))
paychoice = int(input('Forma de Pagamento: \n1 Dinheiro \n2 A vista cartao \n3 Parcelado no Cartao: \n'))
if paychoice == 1:
    price = productname * 0.90
    print(f'Valor a pagar: R${price:.2f}')
elif paychoice == 2:
    price = productname * 0.95
    print(f'Valor a pagar: R${price:.2f}')
elif paychoice == 3:
    par = int(input('Quantas vezes?'))
    if par >= 3:
        price = productname * 1.20
        print(f'Valor a Pagar: R${price:.2f}')
    else:
        print(f'Valor a Pagar: R${productname}')
