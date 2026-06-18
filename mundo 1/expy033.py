n1 = float(input('Digite um numero:'))
n2 = float(input('Digite outro numero:'))
n3 = float(input('Digite mais outro numero:'))
if n1 > n2 > n3:
    ma = n1
    mi = n3
    print(f'O numero {ma} e o maior e o numero {mi} o menor')
elif n1 > n3 > n2:
    ma = n1
    mi = n2
    print(f'O numero {ma} e o maior e o numero {mi} o menor')
elif n2 > n1 > n3:
    ma = n2
    mi = n3
    print(f'O numero {ma} e o maior e o numero {mi} o menor')
elif n2 > n3 > n1:
    ma = n2
    mi = n1
    print(f'O numero {ma} e o maior e o numero {mi} o menor')
elif n3 > n1 > n2:
    ma = n3
    mi = n2
    print(f'O numero {ma} e o maior e o numero {mi} o menor')
elif n3 > n2 > n1:
    ma = n3
    mi = n1
    print(f'O numero {ma} e o maior e o numero {mi} o menor')
else:
    print('Não foi possível determinar o maior e menor número:')

# Solução feita sem usar if else:
# nms = [n1, n2, n3]
# nms.sort()A
# print(f'O número maior e {nms[2]} e o menor {nms[0]}')
