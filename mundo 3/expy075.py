num_list = []
for num in range(0, 4):
    numbers = int(input('Digite um numero:'))
    num_list.append(numbers)
tuple_num_list = tuple(num_list)
print(f'O numero 9 aparece {tuple_num_list.count(9)} vezes')
if 3 in tuple_num_list:
    print(f'O numero 3 aparece primeiro na posicao {tuple_num_list.index(3) + 1}')
else:
    print('O numero 3 nao foi digitado')
print('Os numeros pares foram', end=' ')
for par in tuple_num_list:
    if par % 2 == 0:    
        print(par, end=' ')