num = 0
while True:
    num = int(input('Tabuada de qual valor? '))
    for coef in range(1, 11):
        multi = num * coef
        print(f'{num} X {coef} = {multi}')
    if num < 0:
        break