from time import sleep
def title(title):
    print('+' * (len(title) + 30))
    print(title.center(len(title) + 30))
    print('+' * (len(title) + 30))

def people_system():
    while True:
        sleep(0.8)
        title('MENU PRINCIPAL')
        print('1 - Ver Pessoas cadastradas')
        print('2 - Cadastrar uma pessoa')
        print('3 - Sair do Sistema')
        print('+' * 44)
        choice = input('Sua Opcao: ')
        try:
            inter = int(choice)
            if inter == 1:
                sleep(0.8)
                with open('peoples.txt', 'r') as file:
                    files = file.read()
                    print(files)
            if inter == 2:
                sleep(0.8)
                add_person()
            if inter == 3:
                return
        except:
            print('Nao e uma OPCAO VALIDA')

def add_person():
    lst = []
    title('NOVO CADASTRO')
    while True:
        name = input('Nome: ')
        if not name:
            print('NADA FOI DIGITADO TENTE NOVAMENTE')
            continue
        while True:
            age = input('Idade: ')
            try:
                age = int(age)
                if age < 0:
                    raise ValueError
                break
            except:
                print('NAO E UMA IDADE VALIDA, DIGITE NOVAMENTE')
        lst.append([name, age])
        with open('peoples.txt', 'a', encoding='utf-8') as file:
            for people in lst:
                n = people[0]
                i = people[1]
                file.write(f'{n:<35} {i} Anos\n')
            lst.clear()
        return