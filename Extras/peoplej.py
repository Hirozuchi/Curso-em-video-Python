from time import sleep
import json
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
                with open('people.json', 'r') as file:
                    json_file = json.load(file)
                    print(json_file)
            if inter == 2:
                sleep(0.8)
                add_person()
            if inter == 3:
                return
        except:
            print('Nao e uma OPCAO VALIDA')

def add_person():
    data = {}
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
        data['name'] = name
        data['age'] = age
        try:
            with open('people.json', 'r') as json_file:
                dict_j = json.load(json_file)
                if not isinstance(dict_j, list):
                    dict_j = []
        except FileNotFoundError:
            dict_j = []
        dict_j.append(data.copy())
        with open('people.json', 'w') as json_file:
            json.dump(dict_j, json_file, indent=4, ensure_ascii=False)
        data.clear()
        return