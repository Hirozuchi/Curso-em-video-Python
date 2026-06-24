numbers = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
num = 0
while True: 
    num = int(input('Digite um Numero entre 0 e 20: '))
    if num >= 0 and num <= 20:
        print(f'Numero digitado: {numbers[num]}')
        break
    else:
        print('Tente Novamente', end=' ')