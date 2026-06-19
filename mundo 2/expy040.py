n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
md = (n1 + n2) / 2
if md < 5:
    print(f'Sua media foi {md:.1f}, REPROVADO')
elif md >= 5 and md <= 6.9:
    print(f'Sua media foi {md:.1f}, RECUPERACAO')
elif md >= 7:
    print(f'Sua media foi {md:.1f}, APROVADO')