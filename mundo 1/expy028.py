import random
print('JOGO DO ADIVINHO')
pc = random.randrange(0, 5)
p1 = int(input('Pensei em um número entre 0 a 5, Qual número pensei?'))
if p1 == pc:
    print(f'Sim! o número que pensei foi {pc}, Parabéns!')
elif p1 > 5:
    print('Esse número está fora do que adivinhei')
else:
    print(f'Errado! o número que pensei foi {pc}, tente novamente!')
