'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

while True:
    n = int(input('\nInforme a tabuada que deseja visualizar: '))
    if n >= 0:
        i = 0
        while i <= 10:
            resultado = n * i
            print(f'{n} x {i:2} = {resultado:2}')
            i += 1
    else:
        break