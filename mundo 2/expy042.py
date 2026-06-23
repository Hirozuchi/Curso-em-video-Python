side1 = float(input('Digite o comprimento do primeiro lado:'))
side2 = float(input('Digite o comprimento do segundo lado:'))
side3 = float(input('Digite o comprimento do terceiro lado:'))
sidelst = [side1, side2, side3]
sidelst.sort()
if sidelst[0] + sidelst[1] >= sidelst[2]:
    if side1 == side2 == side3:
        print('Os lados formam um triangulo equilatero')
    elif side1 == side2 or side2 == side3 or side3 == side1:
        print('os lados formam um triangulo isoceles')
    else:
        print('Os lados formam um triangulo escaleno')
else:
    print('Os lados nao formam um triangulo')
