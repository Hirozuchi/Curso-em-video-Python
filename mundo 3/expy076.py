product_tuple = ('Pao', 3.50, 'Lapis', 2, 'Alcatra', 88, 'Uranio', 6700, 'Drone', 2539.99, 'Motor Eletrico', 3434, 'Bala', 0.50, 'Relogio', 449.99)
for i in range(0, len(product_tuple), 2):
    print(f'{product_tuple[i].ljust(20, '.')} R${product_tuple[i+1]:.2f}')