l1 = float(input('Digite o comprimento do primeiro lado:'))
l2 = float(input('Digite o comprimento do segundo lado:'))
l3 = float(input('Digite o comprimento do terceiro lado:'))
if l1 < l3 and l2 < l3 and l1 + l2 > l3:
    print('Os lados formam um triângulo')
elif l1 < l2 and l3 < l2 and l1 + l3 > l2:
    print('Os lados formam um triângulo')
elif l2 < l1 and l3 < l1 and l2 + l3 > l1:
   print('Os lados formam um triângulo')
else:
    print('Os lados não formam um triângulo')