num_list = []
while True:
    num = int(input('Digite um Valor:'))
    if num not in num_list:
        print('Valor Adicionado')
        num_list.append(num)
    else:
        print('Valor Duplicado, Nao adicionado')
    yes_no = ' '
    while yes_no not in 'SN':
        yes_no = input('Quer continuar [S/N] ').upper()
    if yes_no == 'N':
        break
num_sorted = num_list.sort()
print(f'Valores digitados: {num_list}')