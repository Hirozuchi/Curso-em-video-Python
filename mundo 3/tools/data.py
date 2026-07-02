def read_money(money):
    while True:
        p = input(money)
        np = p.replace(',', '.')
        try:
            price = float(np)
            return price
        except ValueError:
            print(f'ERRO: {p} e uma valor invalido!')