#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistaar
#Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
year = int(datetime.date.today().year)

ano_nascimento = int(input('Informe o ano de nascimento (YYYY): '))
anos = year - ano_nascimento

if anos < 18:
    print('Você ainda vai se alistar. Faltam {} anos para se alistar!'.format(18 - anos))
elif anos == 18:
    print('Já é hora de se alistar!')
else:
    print('Já passou da hora de se alistar! Você deveria ter se alistado há {} anos.'.format(anos - 18))