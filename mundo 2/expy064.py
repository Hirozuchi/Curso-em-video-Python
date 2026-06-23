num = 0
lst = []
coef = 0
while num != 999:
    num =int(input('Numero inteiro: '))
    lst.append(num)
    coef += 1
total = sum(lst) - 999
print(f'Numeros digitados: {coef} \n Soma dos Numeros:{total}')