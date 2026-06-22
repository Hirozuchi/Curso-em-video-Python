s = 0
while s == 0:
    sex = input('Digite seu Sexo (M/F): ')
    if sex.upper() == 'M':
        print('Seu sexo e masculino')
        s += 1
    elif sex.upper() == 'F':
        print('Seu sexo e feminino')
        s+= 1
    else:
        print('Nao e uma valor valido, digite novamente')