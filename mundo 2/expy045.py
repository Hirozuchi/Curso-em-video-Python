import random
import time
ppt = random.randint(1, 3)
def tm(): #Delay Before results
    time.sleep(0.5)
    print('じゃん')
    time.sleep(0.5)
    print('けん')
    time.sleep(0.5)
    print('ポン!')
    time.sleep(0.5)
l = ['PEDRA', 'PAPEL', 'TESOURA']
print('Pedra, Papel e Tesoura!')
print('Instrucoes: Escolha entre \n[1]Pedra \n[2]Papel \n[3]Tesoura')
jg = int(input('Qual a SUA ESCOLHA:'))
tm()
if jg == 1: #Player plays Rock
    if jg == ppt:
        print(f'O computador jogou {l[0]} \n Jogador jogou {l[0]} \n EMPATE')
    elif ppt == 2:
        print(f'O Computador jogou {l[1]} \nO jogador jogou {l[0]} \nDERROTA DO JOGADOR')
    else:
        print(f'O Computador jogou {l[2]} \nO jogador jogou {l[0]} \nVITORIA DO JOGADOR')
elif jg == 2: #Player plays Paper
    if jg == ppt:
        print(f'O computador jogou {l[1]} \n Jogador jogou {l[1]} \n EMPATE')
    elif ppt == 3:
        print(f'O Computador jogou {l[2]} \nO jogador jogou {l[1]} \nDERROTA DO JOGADOR')
    else:
        print(f'O Computador jogou {l[0]} \nO jogador jogou {l[1]} \nVITORIA DO JOGADOR')
else: #Player plays Scissors
    if jg == ppt:
        print(f'O computador jogou {l[2]} \n Jogador jogou {l[2]} \n EMPATE')
    elif ppt == 1:
        print(f'O Computador jogou {l[1]} \nO jogador jogou {l[2]} \nDERROTA DO JOGADOR')
    else:
        print(f'O Computador jogou {l[0]} \nO jogador jogou {l[2]} \nVITORIA DO JOGADOR')