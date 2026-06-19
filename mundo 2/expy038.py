n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))
if n1 > n2:
    print(f'O numero {n1} e maior que {n2}')
elif n2 > n1:
    print(f'O numero {n2} e maior que {n1}')
elif n1 == n2:
    print('Os numeros sao iguais')
