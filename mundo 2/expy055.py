l = []
for i in range(0, 5):
    ps = float(input('Peso:'))
    l.append(ps)
mx = max(l)
mn = min(l)
print(f'Maior Peso:{mx:.1f} \nMenor Peso:{mn:.1f}')
