value = 0
term = int(input('Primeiro termo da PA: '))
ratio = int(input('Razao: '))
while value < 10:
    value += 1
    term += ratio
    print(term, end=' ')