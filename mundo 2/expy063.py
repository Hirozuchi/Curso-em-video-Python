num= int(input('termos para mostrar: '))
term1 = 0
term2 = 1
total = 0
while total <= (num + 1):
   print(total, end=' ')
   term1 = term2
   term2 = total
   total = term1 + term2
'''
f = [0, 1]
for i in range(2, n):
   f.append(f[-1] + f[-2])
print(f)'''