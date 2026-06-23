phrase = input('Frase:')
phrasessplit = phrase.split()
reverselst = []
for i in range(len(phrase) -1, -1, -1):
    reverselst.append(phrase[i])
reversephrase = ''.join(reverselst)
phraselstjoin= ''.join(phrase)
if reversephrase.lower() == phraselstjoin.lower():
    print(f'A Frase:"{phrase}", e um palidromo')
else:
    print(f'A frase {phrase} nao e um palidromo pois seu inverso e {reversephrase}')