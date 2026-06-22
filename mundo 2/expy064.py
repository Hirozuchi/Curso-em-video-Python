n = 0
l = []
q = 0
while n != 999:
    n =int(input('Numero inteiro: '))
    l.append(n)
    q += 1
t = sum(l) - 999
print(f'Numeros digitados: {q} \n Soma dos Numeros:{t}')