import random
from time import sleep
player1 = 0
value = 0
result = 0
print('JOGO PAR OU IMPAR')
while True:
    evenuneven = ' '
    cpu = random.randint(1, 10)
    value = int(input('Digite um Valor: '))
    while ty not in 'PI':
        ty = input('Par ou Impar [P/I]: ').upper()
    result = cpu + value
    if evenuneven.upper() == 'P':
        if result % 2 == 0:
            player1 += 1
            print(f'Jogador jogou {value}, o Computador {cpu}, Total {result} deu PAR \n VITORIA DO JOGADOR')
            print('Vamos Jogar Novamente')
            sleep(1)
        else:
            print(f'Jogador jogou {value}, Computador {cpu}, Total: {result} deu INPAR \n VITORIA DO COMPUTADOR')
            print(f'Pontuacao do Jogador: {player1}')
            break
    elif evenuneven.upper() == 'I':
        if result % 2 != 0:
            player1 += 1
            print(f'Jogador jogou {value}, o Computador {cpu}, Total {result} deu IMPAR \n VITORIA DO JOGADOR')
            print('Vamos Jogar Novamente')
            sleep(1)
        else:
            print(f'Jogador jogou {value}, Computador {cpu}, Total: {result} deu PAR \n VITORIA DO COMPUTADOR')
            print(f'Pontuacao do Jogador: {player1}')
            break