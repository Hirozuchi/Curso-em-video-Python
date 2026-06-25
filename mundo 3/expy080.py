num_list = []
for count in range(0, 5):
    num = int(input('Digite um Valor: '))
    if count == 0 or num > num_list[-1]:
        num_list.append(num)
        print('Valor adicionado Final da Lista')
    else:
        pos = 0
        while pos < len(num_list):
            if num <= num_list[pos]:
                num_list.insert(pos, num)
                print(f'Valor adicionado na posicao {pos}')
                break
            pos += 1
print(f'Valores digitados: {num_list}')