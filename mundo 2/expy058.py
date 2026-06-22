import random
pc = random.randrange(0, 10)
p1 = 0
cpu = 0
ex = 0
tent = 0
retry = 0
while ex == 0:
    pl = int(input('Qual numero entre 0 e 10 eu pensei? '))
    if pl == pc:
        print(f'Voce ACERTOU eu pensei no numero {pc} \nTentativas ate acertar nessa rodada: {tent}')
        p1 += 1
        retry = 0
        print(f'Jogador:{p1} =+= Computador:{cpu}')
        while retry == 0:
            cn = input('Quer Continuar? [S/N]: ')
            if cn.upper() == 'N':
                ex += 1
                retry += 1
            elif cn.upper() == 'S':
                retry += 1
            else:
                print('Nao e um valor valido digite novamente') 
    else:
        print(f'Voce errou o Numero que pensei foi {pc}!')
        cpu += 1
        tent += 1
        print(f'Jogador:{p1} =+= Computador:{cpu}')
        print('Tente Novamente!')
