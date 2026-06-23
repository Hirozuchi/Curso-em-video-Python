agesum = 0
names = [] # Nomens
agemen = [] #Idade Homems
agefem = [] # Idades Mulheres
namemen = [] # Nomes Homens
namefem = [] # Nomes Mulheres
men20 = 0 # Homens com menos de 20
fem20 = 0 # Mulheres com menos de 20
men20 = 0 #Homems com mais de 20
fem20 = 0 # Mulheres com mais de 20
size = int(input('Quantas pessoas? '))
for i in range(1, size + 1):
    print(f'++__++ {i} Pessoa ++__++')
    name = input('Nome:')
    age = int(input('Idade:'))
    sex = input('Sexo [M/F]:')
    agesum += age
    names.append(name)
    if sex.upper() == 'F':
        agefem.append(age)
        namefem.append(name)
        if age < 20:
            fem20 += 1
        else:
            fem20 += 1
    elif sex.upper() == 'M':
        agemen.append(age)
        namemen.append(name)
        if age < 20:
            men20 +=1
        else:
            men20 +=1
ageavg = agesum / len(names) #Media das idades
#Achar nome e idade do mais velho
oldagem = max(agemen)
oldestman = agemen.index(oldagem)
#Nome e idade da mais velha
oldagef = max(agefem)
oldestwoman = agefem.index(oldagef) 
print(f'Media das idades do grupo:{ageavg}')
print(f'Homem mais velho:{namemen[oldestman]} \nIdade do Homem mais velho:{oldagem} \nHomens com menos de 20:{men20} \nHomens mais de 20:{men20}')
print(f'Mulheres Com Menos de 20:{fem20} \nMulher mais velha:{namefem[oldestwoman]} \nIdade da Mais velha:{oldagef} \nMulheres mais de 20:{fem20}')