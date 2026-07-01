from colorama import Fore, Back, Style, init
init()

def title(msg, color):
    if color == 'cyan':
        print(Back.CYAN, end='')
    if color == 'magenta':
        print(Back.MAGENTA, end='') 
    if color == 'red':
        print(Back.RED, end='')
    size = len(msg) + 4
    print('=' * size)
    print(f'    {msg}')
    print('=' * size)
    print(Style.RESET_ALL)

def helper(valor):
    title(f'Acessing Manual of command {valor}', 'magenta')
    print(Back.WHITE,Fore.BLACK)
    help(valor)

def help_finder():
    while True:
        title('HELP FINDER PYTHON', 'cyan')
        value = input('Function or Library: ')
        if value.upper() == 'FIM':
            title('END', 'red')
            break
        helper(value)
        
help_finder()