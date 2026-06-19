from datetime import datetime
nas = int(input('Digite o seu Ano de nascimento: '))
ano = datetime.now().year
id = ano - nas
ame = ano + (-id - 18)
ama = ano - (id - 18)
if id < 18:
    print(f'Quem nasceu em {nas} possui {id} anos em {ano}). \nSeu alistamento sera no ano {ame}')
elif id > 18:
    print(f'Quem nasceu em {nas} possui {id} anos em {ano}. \nSeu alistamento esta atrasado {ano - ama} ano(s) \nSeu alistamento foi em {ama}') 
elif id == 18:
    print(f'Quem nasceu em {nas} possui {id} anos em {ano}. \n Seu Alistamento e no ano atual ({ano})')