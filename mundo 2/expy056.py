sid = 0
l = [] # Nomens
lim = [] #Idade Homems
lif = [] # Idades Mulheres
lm = [] # Nomes Homens
lf = [] # Nomes Mulheres
mn = 0 # Homens com menos de 20
fn = 0 # Mulheres com menos de 20
m = 0 #Homems com mais de 20
f = 0 # Mulheres com mais de 20
vz = int(input('Quantas pessoas? '))
for i in range(1, vz + 1):
    print(f'++__++ {i} Pessoa ++__++')
    nm = input('Nome:')
    id = int(input('Idade:'))
    sx = input('Sexo [M/F]:')
    sid += id
    l.append(nm)
    if sx.upper() == 'F':
        lif.append(id)
        lf.append(nm)
        if id < 20:
            fn += 1
        else:
            f += 1
    elif sx.upper() == 'M':
        lim.append(id)
        lm.append(nm)
        if id < 20:
            mn +=1
        else:
            m +=1
idm = sid / len(l) #Media das idades
#Achar nome e idade do mais velho
im = max(lim)
imd = lim.index(im)
#Nome e idade da mais velha
idf = max(lif)
ifd = lif.index(idf) 
print(f'Media das idades do grupo:{idm}')
print(f'Homem mais velho:{lm[imd]} \nIdade do Homem mais velho:{im} \nHomens com menos de 20:{mn} \nHomens mais de 20:{m}')
print(f'Mulheres Com Menos de 20:{fn} \nMulher mais velha:{lf[ifd]} \nIdade da Mais velha:{idf} \nMulheres mais de 20:{f}')