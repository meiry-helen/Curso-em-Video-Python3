'''Crie um programa que leia o nome e preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000,00.
C) Qual é o nome do produto mais barato.'''

total = 0
qtd_produtos = 0
qtd_produtos1000 = 0
produto_barato = ''
produto_barato_menor = 0
continuar = 'S'

while continuar == 'S':
    continuar = ''
    nome_produto = str(input('PRODUTO: ')).title()
    preço = float(input('PREÇO: R$ '))
    total += preço
    qtd_produtos += 1
    if qtd_produtos == 1:
        produto_barato_menor = preço
    if produto_barato_menor > preço:
        produto_barato_menor = preço
        produto_barato = nome_produto
    if preço > 1000:
        qtd_produtos1000 += 1
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar [S/N]: ')).upper()[0]
        print('\n')
        if continuar == 'N':
            break
print(f'Total da compra: R$ {total:.2f}')
print(f'{qtd_produtos1000} produtos custaram mais de RS 1000.00.')
print(f'{produto_barato} foi o produto mais barato.')
