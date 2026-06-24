num_list = []
par_list = []
for num in range(0, 4):
    numbers = int(input('Digite um numero:'))
    num_list.append(numbers)
    if num % 2 == 0:
        par_list.append(num)
tuple_num_list = tuple(num_list)
print(f'O numero 9 aparece {tuple_num_list.count(9)} vezes')
for count in range(0, len(tuple_num_list)):
    while tuple_num_list[count] == 3:
        print(f'O numero tres aparece primeiro na posicao {tuple_num_list.index(tuple_num_list[count] ) + 1}')
        break
if 3 not in tuple_num_list:
    print('O numero 3 nao foi digitado')
print(F'Os numeros pares foram {par_list}')

