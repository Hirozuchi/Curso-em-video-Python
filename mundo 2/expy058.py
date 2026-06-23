import random
randnum = random.randrange(0, 10)
playerpoint = 0
cpupoint = 0
count = 0
trys = 0
retry = 0
while count == 0:
    playerinput = int(input('Qual numero entre 0 e 10 eu pensei? '))
    if playerinput == randnum:
        print(f'Voce ACERTOU eu pensei no numero {randnum} \nTentativas ate acertar nessa rodada: {trys}')
        playerpoint += 1
        retry = 0
        print(f'Jogador:{playerpoint} =+= Computador:{cpupoint}')
        while retry == 0:
            yesorno = input('Quer Continuar? [S/N]: ')
            if yesorno.upper() == 'N':
                count += 1
                retry += 1
            elif yesorno.upper() == 'S':
                retry += 1
            else:
                print('Nao e um valor valido digite novamente') 
    else:
        print(f'Voce errou o Numero que pensei foi {randnum}!')
        cpupoint += 1
        trys += 1
        print(f'Jogador:{playerpoint} =+= Computador:{cpupoint}')
        print('Tente Novamente!')
