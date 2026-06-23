height = float(input('Altura:'))
weight = float(input('Peso:'))
imc = weight / (height ** 2)
if imc < 18.5:
    print(f'IMC:{imc:.2f} \nAbaixo do Peso')
elif 18.5 <= imc < 25:
    print(f'IMC:{imc:.2f} \nPeso ideal')
elif 25 <= imc < 30:
    print(f'IMC:{imc:.2f} \nSobrepeso')
elif 30 <= imc < 40:
    print(f'IMC:{imc:.2f} \nObesidade')
else:
    print(f'IMC:{imc:.2f} \nObesidade Morbida')