count = 0
value1 = float(input('Valor 1: '))
value2 = float(input('Valor 2: '))
while count == 0:
    operation = int(input('[1]Somar \n[2]Multiplicar  \n[3]Maior \n[4]Outros numeros \n[5]Sair do Programa \n'))
    if operation == 1:
        total = value1 + value2
        print(f'Valor da Soma: {total}')
    elif operation == 2:
        multi = value1 * value2
        print(f'{value1} X {value2} = {multi}')
    elif operation == 3:
        lst = [value1, value2]
        lst.sort()
        print(F'Numero maior: {lst[-1]}')
    elif operation == 4:
        value1 = float(input('Valor 1: '))
        value2 = float(input('Valor 2: '))
    elif operation == 5:
        count += 1
    else:
        print('nao e uma opcao valida escolha entre 1 a 5')