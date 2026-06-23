from datetime import datetime
birthyear = int(input('Digite o seu Ano de nascimento: '))
year = datetime.now().year
age = year - birthyear
yearofage = year + (-age - 18)
overage = year - (age - 18)
if age < 18:
    print(f'Quem nasceu em {birthyear} possui {age} anos em {year}). \nSeu alistamento sera no ano {yearofage}')
elif age > 18:
    print(f'Quem nasceu em {birthyear} possui {age} anos em {year}. \nSeu alistamento esta atrasado {year - overage} ano(s) \nSeu alistamento foi em {overage}') 
elif age == 18:
    print(f'Quem nasceu em {birthyear} possui {age} anos em {year}. \n Seu Alistamento e no ano atual ({year})')