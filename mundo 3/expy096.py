def area(x, y):
    ar = x * y
    print(f'A area do terreno {x} X {y} e de {ar}m²')

length = float(input('Largura (m): '))
width = float(input('Comprimento (m): '))
area(length, width)