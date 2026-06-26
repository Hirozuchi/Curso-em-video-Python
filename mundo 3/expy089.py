import tabulate
student_list = []
count = 0
num = 0
while True:
    student = input('Aluno:')
    note1 = float(input('Nota 1:'))
    note2 = float(input('Nota 2: '))
    notesum = (note1 + note2) / 2
    student_list.append([student, [note1, note2], notesum])
    count += 1
    yes_no = ' '
    while yes_no not in 'SN':
        yes_no = input('Quer continuar [S/N] ').upper()
    if yes_no == 'N':
        break
header = ['Posicao','Nome','Notas', 'Media']
print(tabulate.tabulate(student_list, headers=header, tablefmt='grid', showindex=True, floatfmt=".1f"))
while True:
    num = int(input('Mostrar Nota do Aluno (999 interrompe): '))
    if num == 999:
        break
    if num >= 0 and num < len(student_list):
        print(f'Notas de {student_list[num][0]}: {student_list[num][1]}')
    else:
        print('Nao tem esse aluno, digite novamente')