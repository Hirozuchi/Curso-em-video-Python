home = float(input('Qual e o valor da casa?'))
salary = float(input('Qual o salario do comprador?'))
payears = float(input('Quantos anos de pagamento?'))
Parcel = home / (payears * 12)
if Parcel <= salary * 0.3:
    print(f'O Emprestimo foi aprovado, o valor da sua prestacao mensal sera de {Parcel:.2f}')
else:
    print(f'O emprestimo foi negado, o valor da prestacao excede 30% do seu salario')
