import math
count = 0
while count == 0:
    value = int(input('digite Numero inteiro:'))
    if value < 0:
        print('Digite um Numero positivo, Tente novamente')
    else:
        fact = math.factorial(value)
        print(f'O factorial de {value} e {fact}')
        count += 1

'''v1 = int(input('Numero inteiro: '))
if v1 < 0:
    print('Nao e possivel calcular factorial de numero negativo')
else:
    fac = 1
    for i in range(1,v1 + 1):
        fac *= i
    print(f'factorial de {v1}: {fac}')'''