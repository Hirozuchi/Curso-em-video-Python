count = 0
while count == 0:
    sex = input('Digite seu Sexo (M/F): ')
    if sex.upper() == 'M':
        print('Seu sexo e masculino')
        count += 1
    elif sex.upper() == 'F':
        print('Seu sexo e feminino')
        count+= 1
    else:
        print('Nao e uma valor valido, digite novamente')