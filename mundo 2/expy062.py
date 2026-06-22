v = 0
tu = 0
ct = 10
t = int(input('Primeiro termo da PA: '))
r = int(input('Razao: '))
while ct != 0:
    tu = tu + ct
    while v < tu:
        v += 1
        t += r
        print(t, end=' ')
    ct = int(input('\nQuantos termos a mais mostrar: '))
    
    