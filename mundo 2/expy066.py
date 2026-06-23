n = 0
l = []
cont = 0
while True:
    n  = int(input('Digite um Valor (999 para parar): '))
    if n == 999:
        break
    l.append(n)
    cont += 1
t = sum(l)
print(f'Soma dos numeros {t} \n Quantidade de Numeros {cont}')