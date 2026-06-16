import math
an = float(input('Digite um Angulo:'))
r = math.radians(an)
cs = math.cos(r)
sn = math.sin(r)
tn = math.tan(r)
print(f'O seno, cosseno e tangente do angulo {an}, sao respectivamente, {sn:.2f}, {cs:.2f}, {tn:.2f}')