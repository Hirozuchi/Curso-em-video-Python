t1 = int(input('Primeiro termo da PA: '))
rz = int(input('Razao: '))
for a in range(1, 11):
    pa = t1 + (a - 1) * rz
    print(pa, end=' ')