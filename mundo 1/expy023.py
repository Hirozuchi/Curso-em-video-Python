numb = int(input('digite um numero entre 0 e 9999:'))
ns = str(numb)
sprs = ' '.join(ns)
divd = sprs.split()
m = divd[0]
c = divd[1]
d = divd[2]
u = divd[3]
print(f'Milhar:{m} \nCentena:{c} \nDezena:{d} \nUnidade:{u}')