fr = input('Frase:')
lf = fr.split()
rf = []
for i in range(len(fr) -1, -1, -1):
    rf.append(fr[i])
rfj = ''.join(rf)
frj= ''.join(fr)
if rfj.lower() == frj.lower():
    print(f'A Frase:"{fr}", e um palidromo')
else:
    print(f'A frase {fr} nao e um palidromo pois seu inverso e {rfj}')