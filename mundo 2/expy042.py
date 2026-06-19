l1 = float(input('Digite o comprimento do primeiro lado:'))
l2 = float(input('Digite o comprimento do segundo lado:'))
l3 = float(input('Digite o comprimento do terceiro lado:'))
sr = [l1, l2, l3]
sr.sort()
if sr[0] + sr[1] >= sr[2]:
    if l1 == l2 == l3:
        print('Os lados formam um triangulo equilatero')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('os lados formam um triangulo isoceles')
    else:
        print('Os lados formam um triangulo escaleno')
else:
    print('Os lados nao formam um triangulo')