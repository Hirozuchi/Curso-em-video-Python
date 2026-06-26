matrix = [[], [], []]
count = 0
for number in range(0, 9):
    line = number // 3
    column = number % 3
    num = int(input(f'Digite valor [{line}, {column}]:'))
    count += 1
    if count <= 3:
        matrix[0].append(num)
    elif count > 3 and count <=6:
        matrix[1].append(num)
    elif count > 6 and count <=9:
        matrix[2].append(num)

for row in matrix:
    print(*row)