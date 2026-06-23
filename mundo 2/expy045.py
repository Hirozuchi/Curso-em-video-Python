import random
import time
randnum = random.randint(1, 3)
def delayresult(): #Delay Before results
    time.sleep(0.5)
    print('じゃん')
    time.sleep(0.5)
    print('けん')
    time.sleep(0.5)
    print('ポン!')
    time.sleep(0.5)
lst = ['PEDRA', 'PAPEL', 'TESOURA']
print('Pedra, Papel e Tesoura!')
print('Instrucoes: Escolha entre \n[1]Pedra \n[2]Papel \n[3]Tesoura')
choice = int(input('Qual a SUA ESCOLHA:'))
delayresult()
if choice == 1: #Player plays Rock
    if choice == randnum:
        print(f'O computador jogou {lst[0]} \n Jogador jogou {lst[0]} \n EMPATE')
    elif randnum == 2:
        print(f'O Computador jogou {lst[1]} \nO jogador jogou {lst[0]} \nDERROTA DO JOGADOR')
    else:
        print(f'O Computador jogou {lst[2]} \nO jogador jogou {lst[0]} \nVITORIA DO JOGADOR')
elif choice == 2: #Player plays Paper
    if choice == randnum:
        print(f'O computador jogou {lst[1]} \n Jogador jogou {lst[1]} \n EMPATE')
    elif randnum == 3:
        print(f'O Computador jogou {lst[2]} \nO jogador jogou {lst[1]} \nDERROTA DO JOGADOR')
    else:
        print(f'O Computador jogou {lst[0]} \nO jogador jogou {lst[1]} \nVITORIA DO JOGADOR')
elif choice == 3: #Player plays Scissors
    if choice == randnum:
        print(f'O computador jogou {lst[2]} \n Jogador jogou {lst[2]} \n EMPATE')
    elif randnum == 1:
        print(f'O Computador jogou {lst[1]} \nO jogador jogou {lst[2]} \nDERROTA DO JOGADOR')
    else:
        print(f'O Computador jogou {lst[0]} \nO jogador jogou {lst[2]} \nVITORIA DO JOGADOR')
else:
    print('JOGADA INVALIDA')