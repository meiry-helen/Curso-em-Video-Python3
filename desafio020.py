#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
#que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno1 = input('Informe o nome do aluno 1: ')
aluno2 = input('Informe o nome do aluno 2: ')
aluno3 = input('Informe o nome do aluno 3: ')
aluno4 = input('informe o nome do aluno 4: ')

sorteio_apresentacao = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(sorteio_apresentacao)
print('A ordem do sorteio é: ', sorteio_apresentacao)
