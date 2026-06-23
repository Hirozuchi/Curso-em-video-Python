note50 = 0
note20 = 0
note10 = 0
note1 = 0
print('Saque do Banco')
while True:
    v = int(input('Qual Valor a Sacar? R$'))
    mod50 = 0
    mod20 = 0
    mod10 = 0
    if v >= 50:
        div1 = v // 50
        mod50 = v % 50
        note50 += div1
    if mod50 >= 0:
        div2 = mod50 // 20
        mod20 = mod50 % 20
        note20 += div2
    if mod20 >= 0:
        div3 = mod20 // 10
        mod10 = mod20 % 10
        note10 += div3
    if mod10 >= 0:
        div4 = mod10 // 1
        note1 += div4
        break
if note50 != 0:
    print(f'Celulas de R$50: {note50}')
if note20 != 0:
    print(f'Celulas de R$20: {note20}')
if note10 != 0:
    print(f'Celulas de R$10: {note10}')
if note1 != 0:
    print(f'Celulas de R$1: {note1}')
print('FIM DO SAQUE')