en = 0
v1 = float(input('Valor 1: '))
v2 = float(input('Valor 2: '))
while en == 0:
    op = int(input('[1]Somar \n[2]Multiplicar  \n[3]Maior \n[4]Outros numeros \n[5]Sair do Programa \n'))
    if op == 1:
        s = v1 + v2
        print(f'Valor da Soma: {s}')
    elif op == 2:
        m = v1 * v2
        print(f'{v1} X {v2} = {m}')
    elif op == 3:
        l = [v1, v2]
        l.sort()
        print(F'Numero maior: {l[-1]}')
    elif op == 4:
        v1 = float(input('Valor 1: '))
        v2 = float(input('Valor 2: '))
    elif op == 5:
        en += 1
    else:
        print('nao e uma opcao valida escolha entre 1 a 5')