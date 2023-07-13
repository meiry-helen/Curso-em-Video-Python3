'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
sequência Fibonacci
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8'''
import sys

'''n = int(input('Informe quantos elementos da sequência Fibonacci deseja visualizar: '))
i = 0
j = 0
k = 1
r = j + k
while i < n:
    if i < 1:
        print(j, end=' ')
        print(k, end=' ')
    r = j + k
    j = k + r
    k = r + j
    print(r, j, k, end=' ')
    i += 1'''

n = int(input('Informe quantos termos deseja visualizar: '))
i = 0
j = 1
k = 1
if n == 0:
    sys.exit(0)
if n == 1:
    print(i, end=' ')
    n -= 1
if n == 2:
    print(i, j, end=' ')
    n -= 2
if n > 2:
    print(i, j, end=' ')
    n -= 2
    while n > 0:
        print(k, end=' ')
        i = j
        j = k
        k = i + j
        n -= 1
