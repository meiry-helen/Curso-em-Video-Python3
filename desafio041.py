#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
#categoria, de acordo com a idade:
#Até 9 anos: MIRIM / Até 14 anos: INFANTIL / Até 19 anos: JÚNIOR / Até 20 anos: SÊNIOR / Acima: MASTER

import datetime

today = datetime.date.today()
current_year = today.year

ano_nascimento = int(input('Informe o ano de seu nascimento (YYYY): '))
idade = current_year - ano_nascimento

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JÚNIOR')
elif idade == 20:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')