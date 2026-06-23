value = 0
total = 0
count = 10
term = int(input('Primeiro termo da PA: '))
ratio = int(input('Razao: '))
while count != 0:
    term = total + count
    while value < total:
        value += 1
        total += ratio
        print(total, end=' ')
    count = int(input('\nQuantos termos a mais mostrar: '))
    
    