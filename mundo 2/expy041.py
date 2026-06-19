from datetime import datetime
nas = int(input('Digite o Ano de nascimento: '))
idade = datetime.now().year - nas
if idade <= 9:
    print(f'O Atleta possui {idade} anos \nCategoria: MIRIM')
elif idade <= 14:
    print(f'O Atleta possui {idade} anos \nCategoria: INFANTIL')
elif idade <= 19:
    print(f'O Atleta possui {idade} anos \nCategoria: JUNIOR')
elif idade <=25:
    print(f'O Atleta possui {idade} anos \nCategoria: SENIOR')
elif idade > 25:
    print(f'O Atleta possui {idade} anos \nCategoria: MASTER')