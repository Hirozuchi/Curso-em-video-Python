num_list = []
count = 0
while True:
    num = int(input('Digite um Valor:'))
    num_list.append(num)
    count += 1
    yes_no = ' '
    while yes_no not in 'SN':
        yes_no = input('Quer continuar [S/N] ').upper()
    if yes_no == 'N':
        break
num_sorted = num_list.sort(reverse=True)
print(f'Numeros digitados:{count} \nValores: {num_list}')
if 5 in num_list:
    pos_5 = [m5 for m5, pos in enumerate(num_list) if pos == 5]
    print(f'O Numero 5 esta na lista nas posicoes {pos_5}')
    