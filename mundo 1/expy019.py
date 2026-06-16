import random
a1 = input('Primeiro Aluno:')
a2 = input('Segundo Aluno:')
a3 = input('Terceiro Aluno:')
a4 = input('Quarto Aluno:')
alunos = [a1, a2, a3, a4]
r = random.choice(alunos)
print(f'O Escolhido foi {r}')