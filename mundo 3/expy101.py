from datetime import datetime
def vote(birth):
    age = datetime.now().year - birth
    if age < 16:
        print(f'Com a idade {age} o voto e Opcional')
    if age >= 16 and age < 18:
        print(f'Idade {age} voto OPCIONAL')
    if age >= 18 and age < 70:
        print(f'Idade {age} voto OBRIGATORIO')
    if age >= 70:
        print(f'A idade {age} voto OPCIONAL')

year = int(input('Qual sua data de nascimento? '))
vote(year)