def readint(num):
    while True:
        inter = input(num)
        try:
            int(inter)
            return inter
        except:
            print('ERROR Digite um Numero inteiro')

n = readint('Digite um Numero: ')
print(f'Voce digitou numero {n}')