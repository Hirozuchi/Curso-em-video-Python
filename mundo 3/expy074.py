import random
num_list = []
for randmum in range(0, 5):
    cpunum = random.randrange(0, 200)
    num_list.append(cpunum)
tuple_list = tuple(num_list)
print(F'Valores Sorteados: {tuple_list} \nMaior Numero: {max(tuple_list)} \nMenor Numero: {min(tuple_list)}')