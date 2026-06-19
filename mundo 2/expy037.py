num = int(input('Digite um Numero inteiro: '))
base  = int(input('Escolha a base para conversao: \n1 Binario \n2 Octal \n3 Hexadecimal \n'))
if base == 1:
    print(f'A conversao do {num} para base binaria e {bin(num)}')
elif base == 2:
    print(f'A conversao do {num} para base octal e {oct(num)}')
elif base == 3:
    print(f'A conversao do {num} para base hexadecimal e {hex(num)}')
else:
    print('O Valor digitado nao e umas das opcoes, (1 a 3), digite novamente.')