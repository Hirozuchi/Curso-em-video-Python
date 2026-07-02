def read_money(money):
    while True:
        p = input(money)
        np = p.replace(',', '.')
        try:
            price = float(np)
            if price < 0:
                raise ValueError
            return price
        except (ValueError, TypeError):
            print(f'ERRO: {p} e uma valor invalido!')