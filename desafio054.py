#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não antingiram a
#maioridade e quantas já são maiores.

import datetime

maior = 0
menor = 0

for c in range(1, 8):
    ano_nasc = int(input('Informe o ano de nascimento: '))
    c_year = int(datetime.date.today().year)
    if (c_year - ano_nasc) >= 21:
        maior += 1
    else:
        menor += 1
print('Há {} pessoas maiores de 21 anos.'.format(maior))
print('Há {} pessoas menores de 21 anos'.format(menor))
