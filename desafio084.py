'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

pessoas = []
cadastro_peso = []
pesado = leve = 0
while True:
        continuar = ' '
        cadastro_peso.append(str(input('Digite o nome: ')))
        cadastro_peso.append(float(input('Informe o peso: ')))
        if len(pessoas) == 0:
            pesado = leve = cadastro_peso[1]
        else:
            if cadastro_peso[1] > pesado:
                pesado = cadastro_peso[1]
            if cadastro_peso[1] < leve:
                leve = cadastro_peso[1]
        pessoas.append(cadastro_peso[:])
        cadastro_peso.clear()
        while continuar != 'S' and continuar != 'N':
            continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
        if continuar == 'N':
            break
print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {pesado} Kgs. Peso de ', end=' ')
for i in pessoas:
    if i[1] == pesado:
        print(f'[{i[0]}]', end=' ')
print(f'\nO menor peso foi {leve} Kgs. Peso de ', end=' ')
for i in pessoas:
    if i[1] == leve:
        print(f'[{i[0]}]', end=' ')
