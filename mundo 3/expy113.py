def readint(num):
    while True:
        inter = input(num)
        try:
            full = int(inter)
            return full
        except (ValueError, TypeError):
            if not inter:
                print('Nao foi digitado nada')
                value = 0
                return value
            else:
                print('ERROR Digite um Numero inteiro')


def readfloat(number):
    while True:
        floater = input(number)
        try:
            real = float(floater)
            return real
        except (ValueError, TypeError):
            if not floater:
                print('Nao foi digitado nada')
                value = 0
                return value
            else:
                print('Erro! Digite um valor REAL VALIDO')
n = readint('Digite um Numero: ')
r = readfloat('Digite um Real: ')
print(f'Voce digitou numero inteiro {n} e real {r}')