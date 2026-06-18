sa = float(input('Qual é o seu salário?'))
if sa > 1250.00:
    au = sa * 0.10
    sat = sa + au
    print(f'O aumento de seu salário será {au:.2f} reais, após o aumento salário será {sat:.2f} reais')
else:
    au = sa * 0.15
    sat = sa + au
    print(f'O aumento de seu salário será {au:.2f} reais, após o aumento salário será {sat:.2f} reais')