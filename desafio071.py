'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
será o valor a ser sacado (numero inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.'''

valor = int(input('Quanto deseja sacar: '))
while valor != 0:
        resultado_50 = valor // 50
        valor = valor - (resultado_50 * 50)
        if resultado_50 != 0:
                print(f'{resultado_50} cédulas de R$ 50,00')

        resultado_20 = valor // 20
        valor = valor - (resultado_20 * 20)
        if resultado_20 != 0:
                print(f'{resultado_20} cédulas de R$ 20,00')

        resultado_10 = valor // 10
        valor = valor - (resultado_10 * 10)
        if resultado_10 != 0:
                print(f'{resultado_10} cédulas de R$ 10,00')

        if valor > 0:
                print(f'{valor} cédulas de R$ 1,00')
                valor = 0
