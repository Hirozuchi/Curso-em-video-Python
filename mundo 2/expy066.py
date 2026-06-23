num = 0
lst = []
cont = 0
while True:
    num  = int(input('Digite um Valor (999 para parar): '))
    if num == 999:
        break
    lst.append(num)
    cont += 1
total = sum(lst)
print(f'Soma dos numeros {total} \n Quantidade de Numeros {cont}')