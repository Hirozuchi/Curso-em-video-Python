def factorial (num, show=False):
    f = 1
    if show:
        for c in range(num, 0, -1):
            f*=c
            if c == 1:
                print(f'{c}', end='')
            else:
                print(f'{c}', end='x')
        print(f' = {f}')
    else:
        for c in range(num, 0, -1):
            f *= c
        print(f'{f}')

factorial(5, show=True)