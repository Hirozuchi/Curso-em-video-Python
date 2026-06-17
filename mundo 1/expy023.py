numb = int(input('digite um numero entre 0 e 9999:'))
m = numb // 1000 % 10
c = numb // 100 % 10
d = numb // 10 % 10
u = numb // 1 % 10
print(f'Milhar:{m} \nCentena:{c} \nDezena:{d} \nUnidade:{u}')