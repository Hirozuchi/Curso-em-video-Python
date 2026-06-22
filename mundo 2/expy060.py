import math
r = 0
while r == 0:
    v1 = int(input('digite Numero inteiro:'))
    if v1 < 0:
        print('Digite um Numero positivo, Tente novamente')
    else:
        fac = math.factorial(v1)
        print(f'O factorial de {v1} e {fac}')
        r += 1

'''v1 = int(input('Numero inteiro: '))
if v1 < 0:
    print('Nao e possivel calcular factorial de numero negativo')
else:
    fac = 1
    for i in range(1,v1 + 1):
        fac *= i
    print(f'factorial de {v1}: {fac}')'''