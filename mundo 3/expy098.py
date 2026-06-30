from time import sleep
def count(start, end, step):
    co = 0
    if step == 0:
        step = 1
    print(f'Contagem de {start} ate {end} de {step} em {step}')
    if start < end:
        while co <= end:
            if start == 0:
                sleep(0.1)
                print(co, end=' ', flush=True)
                co += 1 * step
            else:
                co += start * (step)
                sleep(0.1)
                print(co, end=' ', flush=True)
    else:
        if step > 0:
            co = start + step
        else:
            co = start + (step * -1)
        while co >= end:
            if step > 0:
                co -= step
                sleep(0.1)
                print(co, end=' ', flush=True)
            else:
                co += step
                sleep(0.1)
                print(co, end=' ', flush=True)
            if co == end:
                break

count(1, 10, 1)
print()
count(10, 0, 2)
print()
print('Agora sua vez de contar!')
star = int(input('Inicio: '))
ed = int(input('Fim: '))
stp = int(input('Passo: '))
count(star, ed, stp)