'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o
menor números digitados e as suas respectivas posições.'''
lista = []
for n in range(0, 5):
    lista.append(int(input('Digite um número: ')))
print(lista)
print(f'O maior valor é {max(lista)} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')
print(f'\nO menor valor é {min(lista)} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')