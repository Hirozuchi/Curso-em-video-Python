total = 0
for i in range(0, 6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        total += num
print(total)