def add_percent(num, per, rs=False):
    if rs:
        return coin(num * (1 + per * 0.01))
    else:
        return num * (1 + per * 0.01)

def minus_percent(num, per , rs=False):
    if rs:
        return coin(num * ( 1 - per * 0.01 ))
    else:
        return num * ( 1 - per * 0.01 )

def half(num, rs=False):
    if rs:
        return coin(num / 2)
    else:
        return num / 2

def double(num, rs=False):
    if rs:
        return coin(num * 2)
    else:
        return num * 2

def coin(value):
    return f'R$ {value:.2f}'.replace('.', ',')

def summary(num, add, minus):
    print('-' * 30)
    print(f'{'Resumo de Valor':^30}')
    print('-' * 30)
    print(f'Preco analisado: {coin(num)}')
    print(f'Dobro do Preco: {double(num, True)}')
    print(f'{add}% de aumento: {add_percent(num, add, True)}')
    print(f'{minus}% de reducao: {minus_percent(num, minus, True)}')
    print('-' * 30)