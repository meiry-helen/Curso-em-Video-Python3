'''Crie um programa que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso'''

from time import sleep
n1 = int(input('Informe um valor: '))
n2 = int(input('Informe outro valor: '))
item = 0
while item != 5:
    item = int(input('\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n\nInforme a operação desejada: '))
    #SOMA
    if item == 1:
        print('\nOPERAÇÃO SOMA\nA soma de {} mais {} é {}\n'.format(n1, n2, n1 + n2))
        sleep(2)
    #MULTIPLICAÇÃO
    elif item == 2:
        print('\nOPERAÇÃO MULTIPLICAÇÃO\nA multiplicação de {} vezes {} é {}\n'.format(n1, n2, n1 * n2))
        sleep(2)
    #MAIOR VALOR
    elif item == 3:
        print('\nOPERAÇÃO MAIOR NÚMERO\n')
        maior = n1
        if n2 > n1:
            print('{} é o maior valor informado.'.format(n2))
            sleep(2)
        else:
            print('{} é o maior valor informado.'.format(n1))
            sleep(2)
    #NOVOS VALORES:
    elif item == 4:
        print('\nOPERAÇÃO NOVOS VALORES\n')
        n1 = int(input('Informe um novo valor: '))
        n2 = int(input('Informe um segundo novo valor: '))
        sleep(2)
print('FIM')
