lst = []
for i in range(0, 5):
    weight = float(input('Peso:'))
    lst.append(weight)
biggerweight = max(lst)
smallestweight = min(lst)
print(f'Maior Peso:{biggerweight:.1f} \nMenor Peso:{smallestweight:.1f}')
