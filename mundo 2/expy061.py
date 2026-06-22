v = 0
t = int(input('Primeiro termo da PA: '))
r = int(input('Razao: '))
while v < 10:
    v += 1
    t += r
    print(t, end=' ')