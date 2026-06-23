from datetime import datetime
birthyear = int(input('Digite o Ano de nascimento: '))
age = datetime.now().year - birthyear
if age <= 9:
    print(f'O Atleta possui {age} anos \nCategoria: MIRIM')
elif age <= 14:
    print(f'O Atleta possui {age} anos \nCategoria: INFANTIL')
elif age <= 19:
    print(f'O Atleta possui {age} anos \nCategoria: JUNIOR')
elif age <=25:
    print(f'O Atleta possui {age} anos \nCategoria: SENIOR')
elif age > 25:
    print(f'O Atleta possui {age} anos \nCategoria: MASTER')