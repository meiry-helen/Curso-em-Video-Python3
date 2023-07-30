'''Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.
B) A soma dos valores na terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
soma_coluna = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe o número da posição {l,c}: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if matriz[l][c] == matriz[l][2]:
            soma_coluna += matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos números pares é: {soma}')
print(f'O maior valor da 2ª linha é: {max(matriz[1])}')
print((f'A soma dos valores da 3ª coluna é: {soma_coluna}'))