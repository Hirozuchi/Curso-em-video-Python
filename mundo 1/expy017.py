import math
ca = float(input("digite o valor do cateto adjacente:"))
co = float(input("digite o valor do cateto oposto:"))
h = math.hypot(ca, co)
print(f'A hipotenusa do triangulo possui o comprimento de {h:.2f}')