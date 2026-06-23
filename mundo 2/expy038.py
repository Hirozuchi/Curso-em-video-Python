num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro numero inteiro: '))
if num1 > num2:
    print(f'O numero {num1} e maior que {num2}')
elif num2 > num1:
    print(f'O numero {num2} e maior que {num1}')
elif num1 == num2:
    print('Os numeros sao iguais')
