num= int(input('Digite um numero:'))
print(f'Tabuada numero {num}:')
for multi in range(1, 11):
    print(f'{num} X {multi} = {num * (multi)}')