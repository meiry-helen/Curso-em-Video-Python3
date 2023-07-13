'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá consultar
se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas têm mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres têm menos de 20 anos.'''

qtd_18 = 0
qtd_homens = 0
qtd_mulheres_20 = 0
continuar = 'S'
sexo = ''
while continuar == 'S':
    continuar = ''
    sexo = ''
    idade = int(input('Informe a idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Informe o sexo [M/F]: ')).upper()[0]
    if idade > 18:
        qtd_18 += 1
    if sexo == 'M':
        qtd_homens += 1
    if sexo == 'F' and idade < 20:
        qtd_mulheres_20 += 1
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar [S/N]: ')).upper()[0]
        print('\n')
    if continuar == 'N':
        break
print(f'Há {qtd_18} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {qtd_homens} homens.')
print((f'Foram cadastradas {qtd_mulheres_20} mulheres com menos de 20 anos.'))
