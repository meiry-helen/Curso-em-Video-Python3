#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
#a média atingida:
#-Média abaixo de 5.0: REPROVADO
#-Média entre 5 e 6.9: RECUPERAÇÃO
#-Média 7 ou superior: APROVADO

n1 = float(input('Informe a nota 1: '))
n2 = float(input('Informe a nota 2: '))
media = (n1 + n2) / 2

if media < 5:
    print('REPROVADO')
elif 7 > media >= 5:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
