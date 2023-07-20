'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número
já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
crescente.'''

lista = []
n = 0

while True:
    continuar = ' '
    n = int(input('Informe um número: '))
    if n not in lista:
        lista.append(n)
        print('Número adicionado à lista com sucesso.')
        while continuar != 'S' and continuar != 'N':
            continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if continuar == 'N':
            break
    else:
        print('Número duplicado!')
        print('Tente novamente!', end=' ')
print(f'Os números informados foram: {sorted(lista)}')
