#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que o ajude, lendo o nome
#deles e escrevendo o nome escolhido.

import random

aluno1 = input('Informe o nome do aluno 1: ')
aluno2 = input('Informe o nome do aluno 2: ')
aluno3 = input('Informe o nome do aluno 3: ')
aluno4 = input('informe o nome do aluno 4: ')

aluno_escolhido = random.choice([aluno1, aluno2, aluno3, aluno4])
print('O aluno escolhido é ', aluno_escolhido)