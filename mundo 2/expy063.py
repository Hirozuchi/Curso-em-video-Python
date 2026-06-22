n = int(input('termos para mostrar: '))
f1 = 0
f2 = 1
s = 0
while s <= (n + 1):
   print(s, end=' ')
   f1 = f2
   f2 = s
   s = f1 + f2
'''
f = [0, 1]
for i in range(2, n):
   f.append(f[-1] + f[-2])
print(f)'''