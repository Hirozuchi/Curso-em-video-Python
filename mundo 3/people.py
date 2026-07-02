import json
from time import sleep

FILE = 'people.json'

def title(text):
    print('+' * (len(title) + 30))
    print(text.center(len(title) + 30))
    print('+' * (len(title) + 30))

def load_people():
    try:
        with open(FILE, 'r') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_people(people):
    with open(FILE, 'w') as f:
        json.dump(people, f, indent=4, ensure_ascii=False)

def ask_int(prompt, min_value=0):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                raise ValueError
            return value
        except ValueError:
            print('Valor invalido, tente novamente.')

def add_person():
    title('NOVO CADASTRO')
    name = input('Nome: ').strip()
    if not name:
        print('NADA FOI DIGITADO.')
        return
    age = ask_int('Idade: ')
    people = load_people()
    people.append({'name': name, 'age': age})
    save_people(people)
    print('Pessoa cadastrada com sucesso!')

def show_people():
    people = load_people()
    print(people if people else 'Nenhuma pessoa cadastrada ainda.')

def people_system():
    options = {1: show_people, 2: add_person}
    while True:
        sleep(0.8)
        title('MENU PRINCIPAL')
        print('1 - Ver Pessoas cadastradas\n2 - Cadastrar uma pessoa\n3 - Sair do Sistema')
        print('+' * 44)
        choice = input('Sua Opcao: ')
        if choice == '3':
            return
        action = options.get(int(choice)) if choice.isdigit() else None
        if action:
            sleep(0.8)
            action()
        else:
            print('Nao e uma OPCAO VALIDA')
