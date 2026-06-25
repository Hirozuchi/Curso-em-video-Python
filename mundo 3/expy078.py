num_list = []
for num in range(0,5):
    number = int(input('Digite um valor'))
    num_list.append(number)
max_num = max(num_list)
min_num = min(num_list)
max_pos = [mx for mx, pos in enumerate(num_list) if pos == max_num]
min_pos = [mn for mn, pos2 in enumerate(num_list) if pos2 == min_num]
print(f'Valores digitados: {num_list} \nMaior Valor: {max_num} na posicoes: {max_pos} \nMenor Valor: {min_num} na Posicoes: {min_pos}')