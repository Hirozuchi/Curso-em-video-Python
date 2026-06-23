n = 0
while True:
    n = int(input('Tabuada de qual valor? '))
    for q in range(1, 11):
        m = n * q
        print(f'{n} X {q} = {m}')
    if n < 0:
        break