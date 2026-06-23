num = 0
count = 0
lst = []
status = 0
while status == 0:
    num =int(input('Numero inteiro: '))
    lst.append(num)
    count = 0
    while count == 0:
        yesorno = input('Quer continuar [S/N]: ')
        if yesorno.upper() == 'N':
            count += 1
            status += 1
        elif yesorno.upper() == 'S':
            status += 1
        else:
            print('digite S OU N')
            
lst.sort()
minnimum = lst[0]
maximum = lst[-1]
avg = sum(lst) / len(lst)  
print(f'Media dos Numeros: {avg} \nNumero Menor:{minnimum} \nNumero Maior: {maximum}')