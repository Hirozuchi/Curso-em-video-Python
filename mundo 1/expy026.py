fra = input('Digite uma Frase:')
cnta = fra.lower().count('a')
first = fra.lower().find('a')+1
last= fra.lower().rfind('a')
print(f'Vezes "A" aparece:{cnta} \nPrimeira Aparição:{first} \nUltima Aparição:{last}')