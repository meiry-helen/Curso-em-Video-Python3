'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint
numeros = []
maior = 0
menor = 21
for c in range(0, 5):
    n = (randint(0, 20))
    numeros.append(n)
tupla_numeros = tuple(numeros)
print('Números sorteados: ', end=' ')
for c in tupla_numeros:
    print(c, end=' ')
    if menor > c:
        menor = c
    if maior < c:
        maior = c
print(f'\nO menor número é {menor} e o maior número é {maior}')

'''Poderiam ser utilizados também os métodos max(tupla_numeros) e min(tupla_numeros) para identificar quais eram o
maior e menor números sorteados.'''
