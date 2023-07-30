'''Crie um programa que crie uma matriz de dimensão 3X3 e preencha com valores lidos pelo teclado.

No final, mostre a matriz na cela, com a formatação correta.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe o número da posição {l,c}: '))
print(matriz)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

'''for c in range(0, 9):
    n = int(input('Informe um número: '))
    if len(matriz[0]) < 3:
        matriz[0].append(n)
    elif len(matriz[1]) < 3:
        matriz[1].append(n)
    else:
        matriz[2].append(n)


for c in matriz[0]:
    print(f'|  {c} ', end=' ')
print('|', sep=' ')
for c in matriz[1]:
    print(f'|  {c} ', end=' ')
print('|', sep=' ')
for c in matriz[2]:
    print(f'|  {c} ', end=' ')
print('|')'''