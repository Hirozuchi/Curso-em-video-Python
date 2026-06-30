import random
from time import sleep
numbers = []
def draw(x):
    for times in range(0, x):
        dr = random.randint(1, 100)
        numbers.append(dr)
    print(f'Sorteando os Valores ', end=' ')
    for num in numbers:
        sleep(0.4)
        print(num, end=' ', flush=True)

def even_sum(lst):
    sum_e = 0
    for even in lst:
        if even % 2 == 0:
            sum_e += even
    print(f'A soma dos valores pares em {lst} é {sum_e}')

draw(5)
even_sum(numbers)