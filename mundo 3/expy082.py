num_list = []
even_list = []
odd_list = []
while True:
    num = int(input('Digite um Valor:'))
    num_list.append(num)
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
    yes_no = ' '
    while yes_no not in 'SN':
        yes_no = input('Quer continuar [S/N] ').upper()
    if yes_no == 'N':
        break
print(f'Numeros: {num_list} \nPares: {even_list} \nImpares: {odd_list}')