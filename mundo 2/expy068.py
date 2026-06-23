import random
from time import sleep
p1 = 0
v = 0
s = 0
print('JOGO PAR OU IMPAR')
while True:
    ty = ' '
    cpu = random.randint(1, 10)
    v = int(input('Digite um Valor: '))
    while ty not in 'PI':
        ty = input('Par ou Impar [P/I]: ').upper()
    s = cpu + v
    if ty.upper() == 'P':
        if s % 2 == 0:
            p1 += 1
            print(f'Jogador jogou {v}, o Computador {cpu}, Total {s} deu PAR \n VITORIA DO JOGADOR')
            print('Vamos Jogar Novamente')
            sleep(1)
        else:
            print(f'Jogador jogou {v}, Computador {cpu}, Total: {s} deu INPAR \n VITORIA DO COMPUTADOR')
            print(f'Pontuacao do Jogador: {p1}')
            break
    elif ty.upper() == 'I':
        if s % 2 != 0:
            p1 += 1
            print(f'Jogador jogou {v}, o Computador {cpu}, Total {s} deu IMPAR \n VITORIA DO JOGADOR')
            print('Vamos Jogar Novamente')
            sleep(1)
        else:
            print(f'Jogador jogou {v}, Computador {cpu}, Total: {s} deu PAR \n VITORIA DO COMPUTADOR')
            print(f'Pontuacao do Jogador: {p1}')
            break