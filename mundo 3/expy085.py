num_list = []
even = []
odd = []
for number in range(1, 8):
    num = int(input(f'Digite {number} valor: '))
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
num_list.append(even[:])
num_list.append(odd[:])
num_list[0].sort()
num_list[1].sort()
print(f'Valor par: {num_list[0]} \nValor Inpar: {num_list[1]}')