num1 = float(input('Nota 1: '))
num2 = float(input('Nota 2: '))
avg = (num1 + num2) / 2
if avg < 5:
    print(f'Sua media foi {avg:.1f}, REPROVADO')
elif avg >= 5 and avg <= 6.9:
    print(f'Sua media foi {avg:.1f}, RECUPERACAO')
elif avg >= 7:
    print(f'Sua media foi {avg:.1f}, APROVADO')