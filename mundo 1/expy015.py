d = int(input('Quantos Dias alugados?'))
km = float(input('Quantos Km rodados?'))
p = d * 60 + km * 0.15
print(f'O total a pagar é {p:.2f} reais')