n = int(input('Numero:'))
if n > 1:
    for pr in range(2, n):
        if n % pr == 0:
            print(f' {n} nao e Primo')
            break
    else:
        print(f'{n} Primo')
else:
    print(f'Nao primo')