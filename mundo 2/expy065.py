n = 0
v = 0
l = []
q = 0
while q == 0:
    n =int(input('Numero inteiro: '))
    l.append(n)
    v = 0
    while v == 0:
        c = input('Quer continuar [S/N]: ')
        if c.upper() == 'N':
            q += 1
            v += 1
        elif c.upper() == 'S':
            v += 1
        else:
            print('digite S OU N')
            
l.sort()
mn = l[0]
ma = l[-1]
m = sum(l) / len(l)  
print(f'Media dos Numeros: {m} \nNumero Menor:{mn} \nNumero Maior: {ma}')