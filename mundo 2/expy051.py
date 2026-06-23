term = int(input('Primeiro termo da PA: '))
ratio = int(input('Razao: '))
for num in range(1, 11):
    pa = term + (num - 1) * ratio
    print(pa, end=' ')