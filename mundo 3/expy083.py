expresion_list = []
expression = input('Digite uma Expressao: ')
expresion_list.append(expression)
valid = 0
for parentesis in expresion_list[0]:
    if parentesis == '(':
        valid += 1
    elif parentesis == ')':
        valid -= 1
    if valid < 0:
        print('Expressao Invalida')
        break
if valid != 0:
    print('Expressao Invalida')
else:
    print(f'Expressao {expresion_list[0]} e valida')