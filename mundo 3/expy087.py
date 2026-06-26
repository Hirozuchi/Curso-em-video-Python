matrix = [[], [], []]
count = 0
even = 0
for number in range(0, 9):
    line = number // 3
    column = number % 3
    num = int(input(f'Digite valor [{line}, {column}]:'))
    count += 1
    if num % 2 == 0:
        even += num
    if count <= 3:
        matrix[0].append(num)
    elif count > 3 and count <=6:
        matrix[1].append(num)
    elif count > 6 and count <=9:
        matrix[2].append(num)
max_line2 = max(matrix[1])
sum_column3 = matrix[0][2] + matrix[1][2] + matrix[2][2]
for row in matrix:
    print(*row)
print('=+=' * 20)
print(f'A soma dos Pares: {even} \nSoma da Terceira coluna:{sum_column3} \nMaior valor segunda linha: {max_line2}')
