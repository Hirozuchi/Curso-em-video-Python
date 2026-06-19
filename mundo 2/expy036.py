ca = float(input('Qual e o valor da casa?'))
sa = float(input('Qual o salario do comprador?'))
ans = float(input('Quantos anos de pagamento?'))
pm = ca / (ans * 12)
if pm <= sa * 0.3:
    print(f'O Emprestimo foi aprovado, o valor da sua prestacao mensal sera de {pm:.2f}')
else:
    print(f'O emprestimo foi negado, o valor da prestacao excede 30% do seu salario')
