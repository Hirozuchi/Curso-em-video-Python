n50 = 0
n20 = 0
n10 = 0
n1 = 0
print('Saque do Banco')
while True:
    v = int(input('Qual Valor a Sacar? R$'))
    m50 = 0
    m20 = 0
    m10 = 0
    if v >= 50:
        d1 = v // 50
        m50 = v % 50
        n50 += d1
    if m50 >= 0:
        d2 = m50 // 20
        m20 = m50 % 20
        n20 += d2
    if m20 >= 0:
        d3 = m20 // 10
        m10 = m20 % 10
        n10 += d3
    if m10 >= 0:
        d4 = m10 // 1
        n1 += d4
        break
print(f'Celulas de R$50: {n50} \nCelulas de R$20: {n20} \nCelulas de R$10: {n10} \nCelulas de R$1: {n1}')
print('FIM DO SAQUE')