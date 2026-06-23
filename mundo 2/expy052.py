num = int(input('Numero:'))
if num > 1:
    for prime in range(2, num):
        if num % prime == 0:
            print(f' {num} nao e Primo')
            break
    else:
        print(f'{num} Primo')
else:
    print(f'Nao primo')