from time import sleep
def bigger(*num):
    print('+_+' * 15)
    print('Analisando Valores....')
    for v in num:
        sleep(0.4)
        print(v, end=' ', flush=True)
    print(f'foram informados {len(num)} ao todo.')
    print(f'O maior Valor foi {max(num)}')
    print('+_+' * 15)
    sleep(0.8)

bigger(5, 3 , 15, 23, 46, 0, 967, 1234, 5)
bigger(2, 3 ,73, 254)
bigger(1, 2 ,578, 345, 9456, 121, 567, 34555, 3456, 3940)
bigger( 7)