'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

produtos = ('Computador', 2500,
            'Televisão', 1900.50,
            'Geladeira', 2690.60,
            'Liquidificador', 250.20,
            'Mesa', 900.98)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^35}')
print('-'*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R$ {produtos[pos]:>7.2f}')
print('-'*40)
